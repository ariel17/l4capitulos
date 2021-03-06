# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    depends_on = (
        ("finance", "0001_initial"),
    )

    def forwards(self, orm):
        # Deleting field 'Book.price'
        db.delete_column(u'book_book', 'price')

        # Adding field 'Book.origin'
        db.add_column(u'book_book', 'origin',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['finance.Purchase'], null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Book.price'
        db.add_column(u'book_book', 'price',
                      self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=10, decimal_places=2),
                      keep_default=False)

        # Deleting field 'Book.origin'
        db.delete_column(u'book_book', 'origin_id')


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
            'editorial': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'isbn': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'origin': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['finance.Purchase']", 'null': 'True', 'blank': 'True'}),
            'published_at': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'quantity': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'summary': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'finance.purchase': {
            'Meta': {'object_name': 'Purchase'},
            'date': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'}),
            'total_items': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['book']
