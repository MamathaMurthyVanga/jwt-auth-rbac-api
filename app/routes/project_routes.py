from fastapi import APIRouter, Depends, HTTPException, status
from app.models.project import Project
from app.schemas.project_schema import ProjectCreate, ProjectRead
from app.dependencies.auth import require_role, get_current_user
from sqlmodel import Session, select
from app.db.database import get_session
from app.db.database import get_session
from fastapi import Query


router = APIRouter()

@router.post("/projects", response_model=ProjectRead)
def create_project(
    project: ProjectCreate,
    session: Session = Depends(get_session),
    current_admin = Depends(require_role("admin"))
):
    db_project = Project(**project.dict())
    session.add(db_project)
    session.commit()
    session.refresh(db_project)
    return db_project



#  View All (admin & user)
@router.get("/projects", response_model=list[ProjectRead])
def get_all_projects(
    session: Session = Depends(get_session),
    current_user = Depends(get_current_user),
    limit: int = Query(10, ge=0),
    offset: int = Query(0, ge=0)
):
    projects = session.exec(select(Project).limit(limit).offset(offset)).all()
    return projects


#  get by id (admin & user)
@router.get("/projects/{project_id}", response_model=ProjectRead)
def get_project(
    project_id: int,
    session: Session = Depends(get_session),
    current_user = Depends(get_current_user)
):
    project = session.get(Project, project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    return project



@router.put("/projects/{project_id}", response_model=ProjectRead)
def update_project(
    project_id: int,
    updated_data: ProjectCreate,
    session: Session = Depends(get_session),
    current_admin = Depends(require_role("admin"))
):
    project = session.get(Project, project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")

    project.name = updated_data.name
    project.description = updated_data.description

    session.add(project)
    session.commit()
    session.refresh(project)
    return project


#  Delete (admin only)
@router.delete("/projects/{project_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_project(
    project_id: int,
    session: Session = Depends(get_session),
    current_admin = Depends(require_role("admin"))
):
    project = session.get(Project, project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")

    session.delete(project)
    session.commit()
    return