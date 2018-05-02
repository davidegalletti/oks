# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-10-19 13:35
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('knowledge_server', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkflowsMethods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_a_placeholder', models.BooleanField(db_column='oks_internals_placeholder', db_index=True, default=False)),
                ('UKCL', models.CharField(blank=True, db_index=True, default='', max_length=750)),
                ('UKCL_previous_version', models.CharField(blank=True, db_index=True, max_length=750, null=True)),
                ('dataset_I_belong_to', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='knowledge_server.DataSet')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_a_placeholder', models.BooleanField(db_column='oks_internals_placeholder', db_index=True, default=False)),
                ('UKCL', models.CharField(blank=True, db_index=True, default='', max_length=750)),
                ('UKCL_previous_version', models.CharField(blank=True, db_index=True, max_length=750, null=True)),
                ('name', models.CharField( max_length=100 )),
                ('description', models.CharField( blank=True, max_length=2000 )),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Attribute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_a_placeholder', models.BooleanField(db_column='oks_internals_placeholder', db_index=True, default=False)),
                ('UKCL', models.CharField(blank=True, db_index=True, default='', max_length=750)),
                ('UKCL_previous_version', models.CharField(blank=True, db_index=True, max_length=750, null=True)),
                ('name', models.CharField(blank=True, max_length=255)),
                ('order', models.IntegerField( null=True ),
                ),

            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AttributeInAMethod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_a_placeholder', models.BooleanField(db_column='oks_internals_placeholder', db_index=True, default=False)),
                ('UKCL', models.CharField(blank=True, db_index=True, default='', max_length=750)),
                ('UKCL_previous_version', models.CharField(blank=True, db_index=True, max_length=750, null=True)),
                ('attribute', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ap.Attribute')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AttributeType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_a_placeholder', models.BooleanField(db_column='oks_internals_placeholder', db_index=True, default=False)),
                ('UKCL', models.CharField(blank=True, db_index=True, default='', max_length=750)),
                ('UKCL_previous_version', models.CharField(blank=True, db_index=True, max_length=750, null=True)),
                ('name', models.CharField(blank=True, max_length=255)),
                ('description', models.TextField( blank=True )),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='KSGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_a_placeholder', models.BooleanField(db_column='oks_internals_placeholder', db_index=True, default=False)),
                ('UKCL', models.CharField(blank=True, db_index=True, default='', max_length=750)),
                ('UKCL_previous_version', models.CharField(blank=True, db_index=True, max_length=750, null=True)),
                ('name', models.CharField(blank=True, max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='KSRole',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_a_placeholder', models.BooleanField(db_column='oks_internals_placeholder', db_index=True, default=False)),
                ('UKCL', models.CharField(blank=True, db_index=True, default='', max_length=750)),
                ('UKCL_previous_version', models.CharField(blank=True, db_index=True, max_length=750, null=True)),
                ('name', models.CharField(blank=True, max_length=255)),
                ('application', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ap.Application')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='KSUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_a_placeholder', models.BooleanField(db_column='oks_internals_placeholder', db_index=True, default=False)),
                ('UKCL', models.CharField(blank=True, db_index=True, default='', max_length=750)),
                ('UKCL_previous_version', models.CharField(blank=True, db_index=True, max_length=750, null=True)),
                ('name', models.CharField(blank=True, max_length=255)),
                ('surname', models.CharField(blank=True, max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PermissionStatement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_a_placeholder', models.BooleanField(db_column='oks_internals_placeholder', db_index=True, default=False)),
                ('UKCL', models.CharField(blank=True, db_index=True, default='', max_length=750)),
                ('UKCL_previous_version', models.CharField(blank=True, db_index=True, max_length=750, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Widget',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_a_placeholder', models.BooleanField(db_column='oks_internals_placeholder', db_index=True, default=False)),
                ('UKCL', models.CharField(blank=True, db_index=True, default='', max_length=750)),
                ('UKCL_previous_version', models.CharField(blank=True, db_index=True, max_length=750, null=True)),
                ('widgetname', models.CharField(blank=True, max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AttributeGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_a_placeholder', models.BooleanField(db_column='oks_internals_placeholder', db_index=True, default=False)),
                ('UKCL', models.CharField(blank=True, db_index=True, default='', max_length=750)),
                ('UKCL_previous_version', models.CharField(blank=True, db_index=True, max_length=750, null=True)),
                ('name', models.CharField(blank=True, max_length=255)),
                ('dataset_I_belong_to', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='knowledge_server.DataSet')),
                ('widgets', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ap.Widget')),
                ('description', models.TextField( blank=True )),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='WorkflowMethod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_a_placeholder', models.BooleanField(db_column='oks_internals_placeholder', db_index=True, default=False)),
                ('UKCL', models.CharField(blank=True, db_index=True, default='', max_length=750)),
                ('UKCL_previous_version', models.CharField(blank=True, db_index=True, max_length=750, null=True)),
                ('name', models.CharField(blank=True, max_length=255)),
                ('description', models.TextField(blank=True)),
                ('create_instance', models.BooleanField(default=False)),
                ('script_precondition', models.TextField(blank=True)),
                ('script_postcondition', models.TextField(blank=True)),
                ('script_premethod', models.TextField(blank=True)),
                ('script_postmethod', models.TextField(blank=True)),
                ('dataset_I_belong_to', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='knowledge_server.DataSet')),
                ('attributes', models.ManyToManyField(through='ap.AttributeInAMethod', to='ap.Attribute')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ApplicationStructureNodeSearch',
            fields=[
                ('id', models.AutoField( auto_created=True, primary_key=True, serialize=False, verbose_name='ID' )),
                ('is_a_placeholder',
                 models.BooleanField( db_column='oks_internals_placeholder', db_index=True, default=False )),
                ('UKCL', models.CharField( blank=True, db_index=True, default='', max_length=750 )),
                ('UKCL_previous_version', models.CharField( blank=True, db_index=True, max_length=750, null=True )),
                ('application', models.ForeignKey( on_delete=django.db.models.deletion.CASCADE, to='ap.Application' )),
                ('dataset_I_belong_to',
                 models.ForeignKey( blank=True, null=True, on_delete=django.db.models.deletion.CASCADE,
                                    related_name='+', to='knowledge_server.DataSet' )),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AttributeInASearch',
            fields=[
                ('id', models.AutoField( auto_created=True, primary_key=True, serialize=False, verbose_name='ID' )),
                ('is_a_placeholder',
                 models.BooleanField( db_column='oks_internals_placeholder', db_index=True, default=False )),
                ('UKCL', models.CharField( blank=True, db_index=True, default='', max_length=750 )),
                ('UKCL_previous_version', models.CharField( blank=True, db_index=True, max_length=750, null=True )),
                ('string_partial', models.BooleanField( )),
                ('string_case_sensitivy', models.BooleanField( )),
                ('integer_interval', models.BooleanField( )),
                ('attribute', models.ForeignKey( on_delete=django.db.models.deletion.CASCADE, to='ap.Attribute' )),
                ('dataset_I_belong_to',
                 models.ForeignKey( blank=True, null=True, on_delete=django.db.models.deletion.CASCADE,
                                    related_name='+', to='knowledge_server.DataSet' )),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ModelMetadataSearch',
            fields=[
                ('id', models.AutoField( auto_created=True, primary_key=True, serialize=False, verbose_name='ID' )),
                ('is_a_placeholder',
                 models.BooleanField( db_column='oks_internals_placeholder', db_index=True, default=False )),
                ('UKCL', models.CharField( blank=True, db_index=True, default='', max_length=750 )),
                ('UKCL_previous_version', models.CharField( blank=True, db_index=True, max_length=750, null=True )),
                ('name', models.CharField( max_length=100 )),
                ('description', models.CharField( blank=True, max_length=2000 )),
                ('dataset_I_belong_to',
                 models.ForeignKey( blank=True, null=True, on_delete=django.db.models.deletion.CASCADE,
                                    related_name='+', to='knowledge_server.DataSet' )),
                ('model_metadata',
                 models.ForeignKey( on_delete=django.db.models.deletion.CASCADE, to='knowledge_server.ModelMetadata' )),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='workflowmethod',
            name='final_status',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='knowledge_server.WorkflowStatus'),
        ),
        migrations.AddField(
            model_name='workflowmethod',
            name='initial_statuses',
            field=models.ManyToManyField(blank=True, related_name='_workflowmethod_initial_statuses_+', to='knowledge_server.WorkflowStatus'),
        ),
        migrations.AddField(
            model_name='workflowmethod',
            name='workflows',
            field=models.ManyToManyField(related_name='methods', through='ap.WorkflowsMethods', to='knowledge_server.Workflow'),
        ),
        migrations.AddField(
            model_name='workflowsmethods',
            name='structure_node',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='knowledge_server.StructureNode'),
        ),
        migrations.AddField(
            model_name='workflowsmethods',
            name='workflow',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='knowledge_server.Workflow'),
        ),
        migrations.AddField(
            model_name='workflowsmethods',
            name='method',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ap.WorkflowMethod'),
        ),
        migrations.AddField(
            model_name='widget',
            name='dataset_I_belong_to',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='knowledge_server.DataSet'),
        ),
        migrations.AddField(
            model_name='permissionstatement',
            name='workflow',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='knowledge_server.Workflow'),
        ),
        migrations.AddField(
            model_name='permissionstatement',
            name='dataset_I_belong_to',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='knowledge_server.DataSet'),
        ),
        migrations.AddField(
            model_name='permissionstatement',
            name='methods',
            field=models.ManyToManyField(blank=True, related_name='permission', to='ap.WorkflowMethod'),
        ),
        migrations.AddField(
            model_name='permissionstatement',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ap.KSGroup'),
        ),
        migrations.AddField(
            model_name='permissionstatement',
            name='role',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ap.KSRole'),
        ),
        migrations.AddField(
            model_name='permissionstatement',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ap.KSUser'),
        ),
        migrations.AddField(
            model_name='ksuser',
            name='dataset_I_belong_to',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='knowledge_server.DataSet'),
        ),
        migrations.AddField(
            model_name='ksuser',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='ksrole',
            name='dataset_I_belong_to',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='knowledge_server.DataSet'),
        ),
        migrations.AddField(
            model_name='ksrole',
            name='users',
            field=models.ManyToManyField(related_name='roles', to='ap.KSUser'),
        ),
        migrations.AddField(
            model_name='ksgroup',
            name='dataset_I_belong_to',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='knowledge_server.DataSet'),
        ),
        migrations.AddField(
            model_name='ksgroup',
            name='users',
            field=models.ManyToManyField(related_name='groups', to='ap.KSUser'),
        ),
        migrations.AddField(
            model_name='attributetype',
            name='dataset_I_belong_to',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='knowledge_server.DataSet'),
        ),
        migrations.AddField(
            model_name='attributetype',
            name='widgets',
            field=models.ManyToManyField(blank=True, to='ap.Widget'),
        ),
        migrations.AddField(
            model_name='attributeinamethod',
            name='dataset_I_belong_to',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='knowledge_server.DataSet'),
        ),
        migrations.AddField(
            model_name='attributeinamethod',
            name='implementation_method',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ap.WorkflowMethod'),
        ),
        migrations.AddField(
            model_name='attribute',
            name='group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ap.AttributeGroup'),
        ),
        migrations.AddField(
            model_name='attribute',
            name='dataset_I_belong_to',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='knowledge_server.DataSet'),
        ),
        migrations.AddField(
            model_name='attribute',
            name='structure_node',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='knowledge_server.StructureNode'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='attribute',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ap.AttributeType'),
        ),
        migrations.AddField(
            model_name='application',
            name='dataset_I_belong_to',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='knowledge_server.DataSet'),
        ),
        migrations.AddField(
            model_name='application',
            name='workflows',
            field=models.ManyToManyField(related_name='applications', to='knowledge_server.Workflow'),
        ),
        migrations.AddField(
            model_name='attributeinamethod',
            name='custom_widget',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ap.Widget'),
        ),
        migrations.AddField(
            model_name='attributeinasearch',
            name='search',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ap.ModelMetadataSearch'),
        ),
        migrations.AddField(
            model_name='applicationstructurenodesearch',
            name='model_metadata_search',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ap.ModelMetadataSearch'),
        ),
        migrations.AddField(
            model_name='applicationstructurenodesearch',
            name='structure_node',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='knowledge_server.StructureNode'),
        ),
    ]