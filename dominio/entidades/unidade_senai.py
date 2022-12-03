from dataclasses import dataclass

from dominio.objetos_de_valor import NomeUnidadeSenai


@dataclass(frozen=True)
class UnidadeSenai:
    nome: NomeUnidadeSenai
