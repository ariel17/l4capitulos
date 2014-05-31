# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'SellByCategory'
        db.create_table(u'totalizer_sellbycategory', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateField')(auto_now=True, blank=True)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['book.Category'])),
            ('total', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
        ))
        db.send_create_signal(u'totalizer', ['SellByCategory'])


    def backwards(self, orm):
        # Deleting model 'SellByCategory'
        db.delete_table(u'totalizer_sellbycategory')


    models = {
        u'book.category': {
            'Meta': {'ordering': "['name', 'parent__id']", 'object_name': 'Category'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['book.Category']", 'null': 'True', 'blank': 'True'})
        },
        u'totalizer.sellbycategory': {
            'Meta': {'object_name': 'SellByCategory'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['book.Category']"}),
            'date': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'total': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['totalizer']
