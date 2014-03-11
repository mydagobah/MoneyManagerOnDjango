# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Spense.issue_date'
        db.alter_column(u'MoneyManager_spense', 'issue_date', self.gf('django.db.models.fields.DateTimeField')())

    def backwards(self, orm):

        # Changing field 'Spense.issue_date'
        db.alter_column(u'MoneyManager_spense', 'issue_date', self.gf('django.db.models.fields.DateField')())

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
            'added_date': ('django.db.models.fields.DateTimeField', [], {}),
            'amount': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'decimal_places': '2'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['MoneyManager.Category']"}),
            'comment': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'null': 'True', 'blank': 'True'}),
            'creditcard': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['MoneyManager.Creditcard']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'issue_date': ('django.db.models.fields.DateTimeField', [], {}),
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