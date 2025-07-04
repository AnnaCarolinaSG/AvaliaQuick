# Generated by Django 5.1.7 on 2025-06-21 19:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('avaliaquick', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Formulario_A',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visao_sistemica', models.PositiveIntegerField(choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4')])),
                ('visao_analitica', models.PositiveIntegerField(choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4')])),
                ('foco_planejamento', models.PositiveIntegerField(choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4')])),
                ('orientacao_mudancas', models.PositiveIntegerField(choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4')])),
                ('relacoes_colaboracao', models.PositiveIntegerField(choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4')])),
                ('total_A', models.FloatField(default=0, null=True)),
                ('avaliacao', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='avaliaquick.pendentes')),
            ],
        ),
        migrations.CreateModel(
            name='Formulario_B',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('presidente_comite', models.PositiveIntegerField(choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')])),
                ('membro_comite', models.PositiveIntegerField(choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')])),
                ('presidente_portifolio', models.IntegerField(choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')])),
                ('membro_portifolio', models.IntegerField(choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')])),
                ('divulgacao_midea', models.IntegerField(choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')])),
                ('formulacao_politicas', models.IntegerField(choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')])),
                ('palestrante_disciplina_pos', models.IntegerField(choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')])),
                ('parcerias_embrapa', models.IntegerField(choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')])),
                ('parcerias_intituicoes', models.IntegerField(choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')])),
                ('responsavel_laboratorio', models.IntegerField(choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')])),
                ('acoes_gerenciais_locais', models.IntegerField(choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')])),
                ('treinamentos_capacitacoes', models.IntegerField(choices=[(4, 'Duas ou mais capacitações e ou treinamentos realizados pelo pesquisador'), (3, 'Uma capacitação e ou treinamento realizada pelo pesquisador'), (0, 'Capacitação não realizada')])),
                ('total_B', models.FloatField(default=0, null=True)),
                ('avaliacao', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='avaliaquick.pendentes')),
            ],
        ),
        migrations.CreateModel(
            name='Formulario_C',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('atuacao_editor', models.IntegerField(choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')])),
                ('clareza_coesao', models.IntegerField(choices=[(4, '100%'), (3, 'Acima de 60%'), (2, 'Entre 40% e 59%'), (1, 'Abaixo de 40%'), (0, 'Nenhum')])),
                ('gestor_contratos', models.IntegerField(choices=[(4, 'Acima de R$ 200 mil'), (3, 'Entre R$ 80 e R$ 200 mil'), (2, 'Até R$ 80 mil'), (1, 'Sem ônus'), (0, 'Sem contrato')])),
                ('lideranca_projeto', models.IntegerField(choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')])),
                ('responsavel_solucao_contribuicao', models.IntegerField(choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')])),
                ('responsavel_atividade', models.IntegerField(choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')])),
                ('participacao_qualificacao', models.IntegerField(choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')])),
                ('coordenacao_propostas_projetos', models.IntegerField(choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')])),
                ('membro_propostas_projetos', models.IntegerField(choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')])),
                ('valor_recursos_financeiros_comprovados', models.IntegerField(choices=[(4, 'Acima de R$ 51 mil'), (3, 'Entre R$ 21 mil e R$ 50 mil'), (2, 'Entre R$ 11 mil e R$ 20 mil '), (1, 'Até R$ 10 mil'), (0, 'Sem captação')], default=0.0)),
                ('instrutor_eventos_tecnicos', models.IntegerField(choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')])),
                ('apresentacao_tecnologias_embrapa', models.IntegerField(choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')])),
                ('responsvel_capacitacao_ead', models.IntegerField(choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')])),
                ('revisor_capacitacao_ead', models.IntegerField(choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')])),
                ('membro_capacitacao_ead', models.IntegerField(choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')])),
                ('coordenador_novas_capacitacoes', models.IntegerField(choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')])),
                ('artigo_a1', models.IntegerField(choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')])),
                ('artigo_a2_a3_a4', models.IntegerField(choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')])),
                ('artigo_b1_b2', models.IntegerField(choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')])),
                ('artigo_b3_inferior', models.IntegerField(choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')])),
                ('producoes_tecnicas_embrapa', models.IntegerField(choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')])),
                ('elaboracao_cap_livros', models.IntegerField(choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')])),
                ('organizacao_edicao_livros', models.IntegerField(choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')])),
                ('artigos_resumos_eventos', models.IntegerField(choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')])),
                ('total_C', models.FloatField(default=0, null=True)),
                ('avaliacao', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='avaliaquick.pendentes')),
            ],
        ),
    ]
