from aplicacao.erros import ErroDocenteNaoEncontrado
from aplicacao.models import ModeloDocente
from dominio.entidades import Docente
from dominio.objetos_de_valor import IdDeDocente
from dominio.repositorios import RepositorioAbstratoDocente


class RepositorioDocente(RepositorioAbstratoDocente):
    def trazer(self) -> [Docente]:
        modelos = ModeloDocente.objects.all()
        return [modelo.para_entidade() for modelo in modelos]

    def trazer_por_id(self, id_: IdDeDocente) -> Docente:
        try:
            modelo = ModeloDocente.objects.get(pk=id_.valor)
            return modelo.para_entidade()
        except ModeloDocente.DoesNotExist:
            raise ErroDocenteNaoEncontrado(id_)

    def salvar(self, docente: Docente) -> None:
        modelo = ModeloDocente.de_entidade(docente)
        modelo.save()

    def deletar_por_id(self, id_: IdDeDocente) -> None:
        pass
