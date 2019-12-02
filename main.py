import os
from peewee import *
from flask import Flask, json, jsonify
from playhouse.shortcuts import model_to_dict

arq = 'clinica.db'
db = SqliteDatabase (arq )

class BaseModel(Model):
    class Meta:
        database = db
        
class Clinica(BaseModel):
    nome = CharField()
    localizacao = CharField()

class Especialidade(BaseModel):
    cod_especialidade = IntegerField()
    documento = CharField()
    desc_especialidade = CharField()        

class Setor(BaseModel):
    nome = CharField()
    localizacao = CharField()
    cor = CharField()
    tipo_setor = CharField()

class Paciente(BaseModel):
    especie = CharField()
    id_paciente = CharField()
    doenca = CharField()
  
class Veterinario(BaseModel):
    nome = CharField()
    id_veterinario = IntegerField()
    salario = FloatField()
    especialidade = ForeignKeyField(Especialidade)

class Requisicao(BaseModel):
    data = CharField()
    paciente = ForeignKeyField(Paciente)
    veterinario = ForeignKeyField(Veterinario)

class Exame(BaseModel):
    preco = FloatField()
    prazo_liberacao = IntegerField()
    nome = CharField()
    
class Exames_requisitados(BaseModel):
    exame = ForeignKeyField(Exame)
    requisicao = ForeignKeyField(Requisicao)

class Dono(BaseModel):
    nome = CharField()
    cpf = CharField()
    tel_contato = CharField()

class Cirurgia(BaseModel):
    nome_cirurgia = CharField()
    data = CharField()
    veterinario_atuante = ForeignKeyField(Veterinario)
    dono = ForeignKeyField(Dono)
    paciente = ForeignKeyField(Paciente)
    setor = ForeignKeyField(Setor)
    duracao = CharField()


if __name__ == "__main__":
    db.connect()
    db.create_tables([Especialidade, Veterinario, Exame, Requisicao, Exames_requisitados, Dono, Cirurgia, Setor, Clinica, Paciente])


    especialidade1 = Especialidade.create(cod_especialidade = 1, documento = "Conselho Federal de Medicina Veterinária - CFMV", desc_especialidade = "Ossos quebrados")
    veterinario1 = Veterinario.create(nome = "Dr. Rosa", id_veterinario = 1, salario = 5400.50, especialidade = especialidade1)
    exame1 = Exame.create(preco = 200, prazo_liberacao = 2, nome = "raio-x")
    paciente1 =  Paciente.create(especie = "cachorro", id_paciente = "1", doenca = "Pata Quebrada")
    requisicao1 = Requisicao.create(data = "10/08/2019", paciente = paciente1, veterinario = veterinario1)
    examerequisicao1 = Exames_requisitados.create(exame = exame1, requisicao = requisicao1)
    dono1 = Dono.create(nome = "Gustavo Costa", cpf = "111.025.79-70", tel_contato = "(47)98808-0581")
    setor1 = Setor.create(nome = "Setor Cirúrgico A1", localizacao = "Prédio A", cor = "Vermelho", tipo_setor = "Cirúrgico")
    cirurgia1 = Cirurgia.create(nome_cirurgia = "Aplicação de pinos na pata", data = "18/12/2019", veterinario_atuante = veterinario1, dono = dono1, paciente = paciente1, setor = setor1, duracao = "2 horas")
    clinica = Clinica.create(nome = "Patas da Vida", localizacao = "Avenida Sete de Setembro 703")

    json = list(map(model_to_dict, Clinica.select()))

    print(json)