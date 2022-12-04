import factory
from factory import fuzzy

from dominio.enums import TipoDeContratacaoEnum
from dominio.otds import OTDDocente
from testes.fabricas.auxiliares import GerarTelefone


class FabricaTesteOTDDocente(factory.Factory):
    class Meta:
        model = OTDDocente

    id = factory.Faker('uuid4', cast_to=None)
    nome = factory.Faker('name')
    email = factory.Faker('email')
    telefone = GerarTelefone.gerar()
    tipo_de_contratacao = fuzzy.FuzzyChoice([opcao for opcao in TipoDeContratacaoEnum])
    unidade_senai_id = factory.Faker('uuid4', cast_to=None)
    ativo = factory.Faker('boolean')
