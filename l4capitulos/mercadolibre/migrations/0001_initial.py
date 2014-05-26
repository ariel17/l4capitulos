# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Item'
        db.create_table(u'mercadolibre_item', (
            ('id', self.gf('django.db.models.fields.CharField')(max_length=20, primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('subtitle', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('price', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=2)),
            ('available_quantity', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('condition', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('permalink', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('thumbnail', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('accepts_mercadopago', self.gf('django.db.models.fields.BooleanField')()),
            ('category_id', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal(u'mercadolibre', ['Item'])


    def backwards(self, orm):
        # Deleting model 'Item'
        db.delete_table(u'mercadolibre_item')


    models = {
        u'mercadolibre.item': {
            'Meta': {'object_name': 'Item'},
            'accepts_mercadopago': ('django.db.models.fields.BooleanField', [], {}),
            'available_quantity': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'category_id': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'condition': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '20', 'primary_key': 'True'}),
            'permalink': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'}),
            'subtitle': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'thumbnail': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['mercadolibre']