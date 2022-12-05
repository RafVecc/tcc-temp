import factory.django
from factory import fuzzy

from aplicacao.models import ModeloDocente
from dominio.enums import TipoDeContratacaoEnum
from testes.fabricas.aplicacao.models.fabrica_teste_modelo_unidade_senai import FabricaTesteModeloUnidadeSenai
from testes.fabricas.auxiliares import GerarTelefone


class FabricaTesteModeloDocente(factory.django.DjangoModelFactory):
    class Meta:
        model = ModeloDocente

    id = factory.Faker('uuid4')
    nome = factory.Faker('name')
    email = factory.Faker('email')
    telefones = str([GerarTelefone.gerar() for _ in range(3)])
    tipo_de_contratacao = fuzzy.FuzzyChoice([opcao.value for opcao in TipoDeContratacaoEnum])
    unidade_senai = factory.SubFactory(FabricaTesteModeloUnidadeSenai)
    ativo = factory.Faker('pybool')
