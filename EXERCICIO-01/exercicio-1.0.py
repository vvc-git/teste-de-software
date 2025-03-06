from datetime import date, datetime, time, timedelta
import unittest



class TestDateMethods(unittest.TestCase):

    # TESTE 1
    def test_cria_data_no_formato_ISO_8601(self):
        # Fixture Setup
        data = date(2002, 12, 3)
        # Exercise SUT (1 FUNÇÃO!)
        data_iso = data.isoformat()
        # Result Verification
        self.assertEqual('2002-12-03', data_iso)
        # Fixture Teardown


    # TESTE 2
    def test_cria_data_no_formato_desejado(self):
        # Fixture Setup
        data = date(2025, 3, 19)
        # Exercise SUT (1 FUNÇÃO!)
        data_formato = data.strftime("%d-%m-%Y")
        # Result Verification
        self.assertEqual('19-03-2025', data_formato)
        # Fixture Teardown

    # TESTE 3
    def test_cria_dia_da_semana_como_inteiro(self):
        # Fixture Setup
        data = date(2025, 3, 19)
        # Exercise SUT (1 FUNÇÃO!)
        dia_semana = data.weekday()
        # Result Verification
        self.assertEqual(2, dia_semana)
        # Fixture Teardown


    # TESTE 4
    def test_cria_dia_da_semana_como_inteiro_no_formato_iso(self):
        # Fixture Setup
        data = date(2025, 3, 19)
        # Exercise SUT (1 FUNÇÃO!)
        dia_semana = data.isoweekday()
        # Result Verification
        self.assertEqual(3, dia_semana)
        # Fixture Teardown


    # TESTE 5
    def test_cria_numero_semana_dia_semana_inteiro_formato_iso(self):
        # Fixture Setup
        data = date(2025, 3, 19)
        # Exercise SUT (1 FUNÇÃO!)
        ano, semana, dia_semana = data.isocalendar()
        # Result Verification
        self.assertEqual(2025, ano)
        self.assertEqual(12, semana)
        self.assertEqual(3, dia_semana)
        # Fixture Teardown


    # TESTE 6
    def test_cria_data_dia_maior_31_invalido(self):
        # Fixture Setup
        # Exercise SUT
        with self.assertRaises(ValueError):
            data_invalida = date(2025, 3, 32)
        # Result Verification
        # Fixture Teardown


    # TESTE 7
    def test_cria_data_mes_negativo_invalido(self):
        # Fixture Setup
        # Exercise SUT
        with self.assertRaises(ValueError):
            data_invalida = date(2025, 3, -1)
        # Result Verification
        # Fixture Teardown


    # TESTE 8
    def test_cria_data_mes_maior_12_invalido(self):
        # Fixture Setup
        # Exercise SUT
        with self.assertRaises(ValueError):
            data_invalida = date(2025, 13, 19)
        # Result Verification
        # Fixture Teardown

    # TESTE 9
    def test_cria_data_ano_negativo_invalido(self):
        # Fixture Setup
        # Exercise SUT
        with self.assertRaises(ValueError):
            data_invalida = date(-2025, -1, 19)
        # Result Verification
        # Fixture Teardown

    # TESTE 10
    def test_combina_data_hora(self):
        # Fixture Setup
        data = date(2025, 3, 19)
        hora = time(14, 35)
        # Exercise SUT (1 FUNÇÃO!)
        data_hora_combinado = datetime.combine(data, hora)
        # Result Verification
        self.assertEqual(2025, data_hora_combinado.year)
        self.assertEqual(3, data_hora_combinado.month)
        self.assertEqual(19, data_hora_combinado.day)
        self.assertEqual(14, data_hora_combinado.hour)
        self.assertEqual(35, data_hora_combinado.minute)
        # Fixture Teardown

    # TESTE 11
    def test_cria_horario_pi(self):
        # Fixture Setup
        # Exercise SUT (1 FUNÇÃO!)
        horario = time(1, 59, 26)
        # Result Verification
        self.assertEqual(1, horario.hour)
        self.assertEqual(59, horario.minute)
        self.assertEqual(26, horario.second)
        # Fixture Teardown
        

    # TESTE 12
    def test_cria_horario_hora_negativo_invalido(self):
        # Fixture Setup
        # Exercise SUT (1 FUNÇÃO!)
        with self.assertRaises(ValueError):
            horario_invalido = time(-1, 59, 26)
        # Result Verification
        # Fixture Teardown

    # TESTE 13
    def test_cria_horario_hora_maior_24_invalido(self):
        # Fixture Setup
        # Exercise SUT (1 FUNÇÃO!)
        with self.assertRaises(ValueError):
            horario_invalido = time(25, 59, 26)
        # Result Verification
        # Fixture Teardown

    # TESTE 14
    def test_cria_horario_minuto_negativo_invalido(self):
        # Fixture Setup
        # Exercise SUT (1 FUNÇÃO!)
        with self.assertRaises(ValueError):
            horario_invalido = time(1, -1, 26)
        # Result Verification
        # Fixture Teardown


    # TESTE 15
    def test_cria_horario_minuto_maior_59_invalido(self):
        # Fixture Setup
        # Exercise SUT (1 FUNÇÃO!)
        with self.assertRaises(ValueError):
            horario_invalido = time(1, 60, 26)
        # Result Verification
        # Fixture Teardown

    # TESTE 16
    def test_cria_horario_segundo_negativo_invalido(self):
        # Fixture Setup
        # Exercise SUT (1 FUNÇÃO!)
        with self.assertRaises(ValueError):
            horario_invalido = time(1, 59, -1)
        # Result Verification
        # Fixture Teardown

    # TESTE 17
    def test_cria_horario_segundo_maior_59(self):
        # Fixture Setup
        # Exercise SUT (1 FUNÇÃO!)
        with self.assertRaises(ValueError):
            horario_invalido = time(1, 59, 60)
        # Result Verification
        # Fixture Teardown

    # TESTE 18
    def test_cria_data_substitui_nova_data(self):
        data = date(2025, 3, 19)
        # Exercise SUT (1 FUNÇÃO!)
        data_substituida = data.replace(2026, 4, 20)
        # Result Verification
        self.assertEqual(2026, data_substituida.year)
        self.assertEqual(4, data_substituida.month)
        self.assertEqual(20, data_substituida.day)
        # Fixture Teardown

    # TESTE 19
    def test_cria_horario_substitui_novo_horario(self):
        # Fixture Setup
        horario = time(1, 59, 26)
        # Exercise SUT (1 FUNÇÃO!)
        horario_substituido = horario.replace(2, 3, 35)
        # Result Verification
        self.assertEqual(2, horario_substituido.hour)
        self.assertEqual(3, horario_substituido.minute)
        self.assertEqual(35, horario_substituido.second)
        # Fixture Teardown

    # TESTE 20
    def test_cria_horario_estilo_ctime(self):
        # Fixture Setup
        data = date(2025, 3, 19)
        # Exercise SUT (1 FUNÇÃO!)
        tupla_horaio = data.ctime()
        # Result Verification
        self.assertEqual('Wed Mar 19 00:00:00 2025', tupla_horaio)
        # Fixture Teardown

    # TESTE 21
    def test_cria_datetime_a_partir_iso_8601(self):
        # Fixture Setup
        data_iso = '2025-03-19'
        # Exercise SUT (1 FUNÇÃO!)
        data_datetime = datetime.fromisoformat(data_iso)
        # Result Verification
        self.assertEqual(2025, data_datetime.year)
        self.assertEqual(3, data_datetime.month)
        self.assertEqual(19, data_datetime.day)
        # Fixture Teardown
        pass

    # TESTE 22
    def test_cria_datetime_a_partir_ano_semana_dia_iso(self):
        # Fixture Setup
        ano = 2025
        semana = 12
        dia_semana = 3
        # Exercise SUT (1 FUNÇÃO!)
        data_datetime = datetime.fromisocalendar(ano, semana, dia_semana)
        # Result Verification
        self.assertEqual(2025, data_datetime.year)
        self.assertEqual(3, data_datetime.month)
        self.assertEqual(19, data_datetime.day)
        # Fixture Teardown

    # TESTE 23
    def test_cria_duas_datas_verifica_igualdade(self):
        # Fixture Setup
        data1 = date(2025, 3, 19)
        data2 = date(2025, 3, 19)
        # Exercise SUT (1 FUNÇÃO!)
        soma = data1 == data2
        # Result Verification
        self.assertEqual(True, soma)

    # TESTE 24
    def test_soma_dias_datetime_deltatime(self):
        # Fixture Setup
        data = date(2025, 3, 19)
        delta = timedelta(10)
        # Exercise SUT (1 FUNÇÃO!)
        soma = data + delta
        # Result Verification
        self.assertEqual(29, soma.day)
    
    # TESTE 25
    def test_subtracao_dias_datetime_deltatime(self):
        # Fixture Setup
        data = date(2025, 3, 19)
        delta = timedelta(10)
        # Exercise SUT (1 FUNÇÃO!)
        soma = data - delta
        # Result Verification
        self.assertEqual(9, soma.day)

if __name__ == '__main__':
    unittest.main()