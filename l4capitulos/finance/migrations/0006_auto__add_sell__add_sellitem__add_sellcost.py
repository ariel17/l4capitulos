# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Sell'
        db.create_table(u'finance_sell', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('price', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=2)),
        ))
        db.send_create_signal(u'finance', ['Sell'])

        # Adding model 'SellItem'
        db.create_table(u'finance_sellitem', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('book', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['book.Book'])),
            ('quantity', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('sell', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['finance.Sell'])),
        ))
        db.send_create_signal(u'finance', ['SellItem'])

        # Adding model 'SellCost'
        db.create_table(u'finance_sellcost', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('price', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=2)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('sell', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['finance.Sell'])),
        ))
        db.send_create_signal(u'finance', ['SellCost'])


    def backwards(self, orm):
        # Deleting model 'Sell'
        db.delete_table(u'finance_sell')

        # Deleting model 'SellItem'
        db.delete_table(u'finance_sellitem')

        # Deleting model 'SellCost'
        db.delete_table(u'finance_sellcost')


    models = {
        u'book.author': {
            'Meta': {'object_name': 'Author'},
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'book.book': {
            'Meta': {'object_name': 'Book'},
            'added_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'authors': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['book.Author']", 'symmetrical': 'False'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['book.Category']", 'null': 'True'}),
            'editorial': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'isbn': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'published_at': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['book.Status']", 'null': 'True'}),
            'summary': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'book.category': {
            'Meta': {'object_name': 'Category'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['book.Category']", 'null': 'True'})
        },
        u'book.status': {
            'Meta': {'object_name': 'Status'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'finance.purchase': {
            'Meta': {'object_name': 'Purchase'},
            'date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'})
        },
        u'finance.purchasecost': {
            'Meta': {'object_name': 'PurchaseCost'},
            'date': ('django.db.models.fields.DateField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'}),
            'purchase': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['finance.Purchase']"})
        },
        u'finance.purchaseitem': {
            'Meta': {'object_name': 'PurchaseItem'},
            'book': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['book.Book']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'purchase': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['finance.Purchase']"}),
            'quantity': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'})
        },
        u'finance.sell': {
            'Meta': {'object_name': 'Sell'},
            'date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'})
        },
        u'finance.sellcost': {
            'Meta': {'object_name': 'SellCost'},
            'date': ('django.db.models.fields.DateField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'}),
            'sell': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['finance.Sell']"})
        },
        u'finance.sellitem': {
            'Meta': {'object_name': 'SellItem'},
            'book': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['book.Book']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'quantity': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'sell': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['finance.Sell']"})
        }
    }

    complete_apps = ['finance']