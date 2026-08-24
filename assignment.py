from pydantic import BaseModel, Field
from fastapi import APIRouter, HTTPException
from datetime import date

router = APIRouter()


class Assignment(BaseModel):
    id: int
    title: str = Field(min_length=3, max_length=100)
    due_date: date
    done: bool


class AssignmentCreate(BaseModel):
    title: str = Field(min_length=3, max_length=100)
    due_date: date
    done: bool = False

class AssignmentUpdate(BaseModel):
    title: str = Field(min_length=3, max_length=100)
    due_date: date
    done: bool


assignments: list[Assignment] = []


@router.post("/assignments",response_model=Assignment,status_code=201)
def create_assignment(payload: AssignmentCreate):
    assignment = Assignment(
        id=len(assignments) + 1,
        title=payload.title,
        due_date=payload.due_date,
        done=payload.done
    )

    assignments.append(assignment)

    return assignment


@router.get("/assignments", response_model=list[Assignment])
def get_assignments(done: bool | None = None):
    if done is None:
        return assignments

    return [assignment for assignment in assignments if assignment.done == done]


@router.get("/assignments/{assignment_id}", response_model=Assignment)
def get_assignment(assignment_id: int):
    for assignment in assignments:
        if assignment.id == assignment_id:
            return assignment

    raise HTTPException(status_code=404, detail="Assignment not found")


@router.put("/assignments/{assignment_id}", response_model=Assignment)
def update_assignment(assignment_id: int, payload: AssignmentUpdate):
    for index, assignment in enumerate(assignments):
        if assignment.id == assignment_id:
            updated_assignment = Assignment(
                id=assignment.id,
                title=payload.title,
                due_date=payload.due_date,
                done=payload.done
            )

            assignments[index] = updated_assignment

            return updated_assignment

    raise HTTPException(status_code=404, detail="Assignment not found")

@router.delete("/assignments/{assignment_id}")
def delete_assignment(assignment_id: int):
    for index, assignment in enumerate(assignments):
        if assignment.id == assignment_id:
            deleted_assignment = assignments.pop(index)
            return deleted_assignment

    raise HTTPException(status_code=404, detail="Assignment not found")