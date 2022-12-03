from dataclasses import dataclass

from dominio.enums import TipoDeContratacaoEnum


@dataclass(frozen=True)
class TipoDeContratacao:
    valor: TipoDeContratacaoEnum
