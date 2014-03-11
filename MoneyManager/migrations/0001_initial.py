# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Category'
        db.create_table(u'MoneyManager_category', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'MoneyManager', ['Category'])

        # Adding model 'SubCategory'
        db.create_table(u'MoneyManager_subcategory', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['MoneyManager.Category'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'MoneyManager', ['SubCategory'])

        # Adding model 'Owner'
        db.create_table(u'MoneyManager_owner', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'MoneyManager', ['Owner'])

        # Adding model 'Creditcard'
        db.create_table(u'MoneyManager_creditcard', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('owner', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['MoneyManager.Owner'])),
        ))
        db.send_create_signal(u'MoneyManager', ['Creditcard'])

        # Adding model 'Income'
        db.create_table(u'MoneyManager_income', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('amount', self.gf('django.db.models.fields.DecimalField')(max_digits=15, decimal_places=2)),
            ('owner', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['MoneyManager.Owner'])),
            ('comment', self.gf('django.db.models.fields.CharField')(max_length=2000, null=True, blank=True)),
        ))
        db.send_create_signal(u'MoneyManager', ['Income'])

        # Adding model 'Spense'
        db.create_table(u'MoneyManager_spense', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('amount', self.gf('django.db.models.fields.DecimalField')(max_digits=15, decimal_places=2)),
            ('issue_date', self.gf('django.db.models.fields.DateField')()),
            ('added_date', self.gf('django.db.models.fields.DateField')()),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['MoneyManager.Category'])),
            ('owner', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['MoneyManager.Owner'])),
            ('subCategory', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['MoneyManager.SubCategory'], null=True, blank=True)),
            ('creditcard', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['MoneyManager.Creditcard'], null=True, blank=True)),
            ('comment', self.gf('django.db.models.fields.CharField')(max_length=2000, null=True, blank=True)),
        ))
        db.send_create_signal(u'MoneyManager', ['Spense'])


    def backwards(self, orm):
        # Deleting model 'Category'
        db.delete_table(u'MoneyManager_category')

        # Deleting model 'SubCategory'
        db.delete_table(u'MoneyManager_subcategory')

        # Deleting model 'Owner'
        db.delete_table(u'MoneyManager_owner')

        # Deleting model 'Creditcard'
        db.delete_table(u'MoneyManager_creditcard')

        # Deleting model 'Income'
        db.delete_table(u'MoneyManager_income')

        # Deleting model 'Spense'
        db.delete_table(u'MoneyManager_spense')


    models = {
        u'MoneyManager.category': {
            'Meta': {'object_name': 'Category'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'MoneyManager.creditcard': {
            'Meta': {'object_name': 'Creditcard'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['MoneyManager.Owner']"})
        },
        u'MoneyManager.income': {
            'Meta': {'object_name': 'Income'},
            'amount': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'decimal_places': '2'}),
            'comment': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['MoneyManager.Owner']"})
        },
        u'MoneyManager.owner': {
            'Meta': {'object_name': 'Owner'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'MoneyManager.spense': {
            'Meta': {'object_name': 'Spense'},
            'added_date': ('django.db.models.fields.DateField', [], {}),
            'amount': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'decimal_places': '2'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['MoneyManager.Category']"}),
            'comment': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'null': 'True', 'blank': 'True'}),
            'creditcard': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['MoneyManager.Creditcard']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'issue_date': ('django.db.models.fields.DateField', [], {}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['MoneyManager.Owner']"}),
            'subCategory': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['MoneyManager.SubCategory']", 'null': 'True', 'blank': 'True'})
        },
        u'MoneyManager.subcategory': {
            'Meta': {'object_name': 'SubCategory'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['MoneyManager.Category']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['MoneyManager']