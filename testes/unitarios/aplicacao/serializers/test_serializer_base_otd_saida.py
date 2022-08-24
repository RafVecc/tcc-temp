from unittest import TestCase

from aplicacao.serializers import SerializerOTDCriarDocenteSaida
from dominio.otds import OTDCriarDocenteSaida
from testes.fabricas.dominio.otds import FabricaTesteOTDCriarDocenteSaida


class TestSerializerOTDCriarDocenteSaida(TestCase):
    def test_dto_para_response_data_QUANDO_otd_informado_ENTAO_retorna_dict_esperado(self) -> None:
        serializer_class = SerializerOTDCriarDocenteSaida
        otd: OTDCriarDocenteSaida = FabricaTesteOTDCriarDocenteSaida.build()

        resultado = serializer_class.otd_para_response_data(otd)

        esperado = {
            'id': otd.id,
            'nome': otd.nome
        }
        self.assertEqual(resultado, esperado)
