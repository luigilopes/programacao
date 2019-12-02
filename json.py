{
    "Clinica":{
        "Especialidade":{
            'id': 1, 
            'cod_especialidade': 1, 
            'documento': 'Conselho Federal de Medicina Veterinária - CFMV',
             'desc_especialidade': 'Ossos quebrados'
        },
        "Veterinario":{
            'id': 1,
            'nome': 'Dr. Rosa', 
            'id_medico': 1, 
            'salario': 5400.5, 
            'especialidade':{
                'id': 1, 
                'cod_especialidade': 1, 
                'documento': 'Conselho Federal de Medicina Veterinária - CFMV', 
                'desc_especialidade': 'Ossos quebrados'
            }
        },
        "Exame":{
            'id': 1, 
            'preco': 200.0, 
            'prazo_liberacao': 2, 
            'nome': 'raio-x'
        },
        "Requisicao":{
            'id': 1, 
            'data': '10/08/2019', 
            'paciente': {
                'id': 1, 
                'especie': 'cachorro', 
                'id_paciente': '1', 
                'doenca': 'Pata Quebrada'
            }, 
            'veterinario': {
                'id': 1, 
                'nome': 'Dr. Rosa', 
                'id_veterinario': 1, 
                'salario': 5400.5, 
                'especialidade': {
                    'id': 1, 
                    'cod_especialidade': 1, 
                    'documento': 'Conselho Federal de Medicina Veterinária - CFMV', 
                    'desc_especialidade': 'Ossos quebrados'
                    }
            }
        },
        "Paciente":{
            'id': 1, 
            'especie': 'cachorro', 
            'id_paciente': '1', 
            'doenca': 'Pata Quebrada'
        },
        "Dono":{
            'id': 1, 
            'nome': 'Gustavo Costa', 
            'cpf': '111.025.79-70', 
            'tel_contato': '(47)98808-0581'
        },
        "Setor":{
            'id': 1, 
            'nome': 'Setor Cirúrgico A1', 
            'localizacao': 'Prédio A', 
            'cor': 'Vermelho', 
            'tipo_setor': 'Cirúrgico'
        },
        "Cirurgia":{
            'id': 1, 
            'nome_cirurgia': 'Aplicação de pinos na pata', 
            'data': '18/12/2019', 
            'veterinario_atuante': {
                'id': 1, 
                'nome': 'Dr. Rosa', 
                'id_veterinario': 1, 
                'salario': 5400.5, 
                'especialidade': {
                    'id': 1, 
                    'cod_especialidade': 1, 
                    'documento': 'Conselho Federal de Medicina Veterinária - CFMV', 
                    'desc_especialidade': 'Ossos quebrados'
                },
            }, 
            'dono': {
                'id': 1, 
                'nome': 'Gustavo Costa', 
                'cpf': '111.025.79-70', 
                'tel_contato': '(47)98808-0581'
            }, 
            'paciente': {
                'id': 1, 
                'especie': 'cachorro', 
                'id_paciente': '1', 
                'doenca': 'Pata Quebrada'
            }, 
            'setor': {
                'id': 1, 
                'nome': 'Setor Cirúrgico A1', 
                'localizacao': 'Prédio A', 
                'cor': 'Vermelho', 
                'tipo_setor': 'Cirúrgico'
            }, 
            'duracao': '2 horas'
        },
        "Clinica":{
            'id': 1, 
            'nome': 'Patas da Vida', 
            'localizacao': 'Avenida Sete de Setembro 703'
        }  
    }
}