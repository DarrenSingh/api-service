from fastapi import APIRouter
from ..models.category import Category
from fastapi import HTTPException, status
from ..database import supabase

router = APIRouter()

# create new category
@router.post("/")
async def create_category():
    # ... implement
    pass

# retrieve all categories
@router.get("/", status_code=status.HTTP_200_OK)
def get_categories():
    try:
        response = supabase.table("categories").select("*").execute()  # Select all columns

        # Convert Supabase response to a list of Pydantic Category objects (optional but recommended)
        categories = []
        for item in response.data:  # response.data contains the actual data
            categories.append(Category(**item)) # Create a Pydantic object

        return categories  # Return the list of categories

    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

# retrieve single category
@router.get("/{id}")
async def get_category(id: int):
    # ... implement
    pass

# update category
@router.put("/{id}")
async def update_category(id: int):
    # ... implement
    pass

# delete category
@router.delete("/{id}")
async def delete_category(id: int):
    # ... implement
    pass
