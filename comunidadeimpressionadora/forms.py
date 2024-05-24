from collections.abc import Sequence
from typing import Any, Mapping
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from comunidadeimpressionadora.models import Usuario
from flask_login import current_user

class FormCriarConta(FlaskForm):
    username = StringField("Nome do usuario", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    senha = PasswordField("Senha", validators=[DataRequired(), Length(6,20)])
    confirmacao_senha = PasswordField("Confirme senha", validators=[DataRequired(), EqualTo('senha')])
    botao_submit_criarconta =  SubmitField("Criar Conta")
    
    def validate_email(self, email):
        usuario = Usuario.query.filter_by(email=email.data).first()
        if usuario:
            raise ValidationError('Email já cadastrado')
        
    

class FormLogin(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    senha = PasswordField("Senha", validators=[DataRequired()])
    lembrar_dados = BooleanField("Lembrar Login")
    botao_submit_login =  SubmitField("Fazer Login")
    
class FormEditarPerfil(FlaskForm):
    username = StringField("Nome do usuario", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    foto_perfil = FileField('Atualizar Foto de Perfil', validators=[FileAllowed(['png', 'jpg'])])
    botao_submit_editarperfil =  SubmitField("Salvar Alterações")
    
    curso_excel = BooleanField("Excel Impressionador")
    curso_python = BooleanField("Python Impressionador")
    curso_sql = BooleanField("SQL Impressionador")
    curso_html = BooleanField("HTML Impressionador")
    curso_css = BooleanField("CSS Impressionador")
    
    def validate_email(self, email):
        if current_user.email != email.data:
            usuario = Usuario.query.filter_by(email=email.data).first()
            if usuario:
                raise ValidationError('Já existe um usuário com este email')
            
            
class FormCriarPost(FlaskForm):
    titulo = StringField('Título do Post', validators=[DataRequired(), Length(2,140)])
    corpo =  TextAreaField('Texto do Post', validators=[DataRequired()])
    botao_submit_criarpost =  SubmitField("Criar Post")