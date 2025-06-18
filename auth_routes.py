from fastapi import APIRouter

auth_router = APIRouter(prefix="/auth", tags=["auth"])

@auth_router.get("/")
async def autenticar():
  """
  Essa é a rota padrão de autenticação do nosso sistema.
  """
  return {"mensagem": "Rota de autenticação", 
          "autenticado": False}
