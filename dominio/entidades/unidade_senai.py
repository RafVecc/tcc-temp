from dataclasses import dataclass

from dominio.objetos_de_valor import NomeUnidadeSenai, Id


@dataclass(frozen=True)
class UnidadeSenai:
    id: Id
    nome: NomeUnidadeSenai
