import factory
from factory import fuzzy

from dominio.enums import TipoDeContratacaoEnum
from testes.fabricas.auxiliares import GerarTelefone
from testes.fabricas.dominio.objetos_de_valor import FabricaTesteNomeDeDocente, FabricaTesteId, FabricaTesteEmail
from dominio.entidades import Docente


class FabricaTesteDocente(factory.Factory):
    class Meta:
        model = Docente

    nome = factory.SubFactory(FabricaTesteNomeDeDocente)
    id_ = factory.SubFactory(FabricaTesteId)
    email = factory.SubFactory(FabricaTesteEmail)
    telefones = str([GerarTelefone.gerar() for _ in range(3)])
    tipo_de_contratacao = fuzzy.FuzzyChoice([opcao.value for opcao in TipoDeContratacaoEnum])
    unidade_senai_id = factory.Faker('uuid4')
    ativo = factory.Faker('boolean')
