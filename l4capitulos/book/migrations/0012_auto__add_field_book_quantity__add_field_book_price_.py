# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Book.quantity'
        db.add_column(u'book_book', 'quantity',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Book.price'
        db.add_column(u'book_book', 'price',
                      self.gf('django.db.models.fields.DecimalField')(default=0, null=True, max_digits=10, decimal_places=2, blank=True),
                      keep_default=False)


        # Changing field 'Book.added_at'
        db.alter_column(u'book_book', 'added_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, null=True))

    def backwards(self, orm):
        # Deleting field 'Book.quantity'
        db.delete_column(u'book_book', 'quantity')

        # Deleting field 'Book.price'
        db.delete_column(u'book_book', 'price')


        # Changing field 'Book.added_at'
        db.alter_column(u'book_book', 'added_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, null=True))

    models = {
        u'book.author': {
            'Meta': {'ordering': "['first_name', 'last_name']", 'unique_together': "(('first_name', 'last_name'),)", 'object_name': 'Author'},
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'book.book': {
            'Meta': {'ordering': "['title']", 'object_name': 'Book'},
            'added_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'authors': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['book.Author']", 'null': 'True', 'blank': 'True'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['book.Category']", 'null': 'True', 'blank': 'True'}),
            'editorial': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['book.Editorial']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'isbn': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'price': ('django.db.models.fields.DecimalField', [], {'default': '0', 'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'published_at': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'quantity': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'status': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['book.Status']", 'null': 'True', 'blank': 'True'}),
            'summary': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'book.bookimage': {
            'Meta': {'object_name': 'BookImage'},
            'book': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['book.Book']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'default': "'img/no-img.png'", 'max_length': '100'}),
            'primary': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'book.category': {
            'Meta': {'ordering': "['name', 'parent__id']", 'object_name': 'Category'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['book.Category']", 'null': 'True', 'blank': 'True'})
        },
        u'book.editorial': {
            'Meta': {'ordering': "['name']", 'object_name': 'Editorial'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'unique': 'True', 'null': 'True', 'blank': 'True'})
        },
        u'book.status': {
            'Meta': {'ordering': "['name']", 'object_name': 'Status'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'})
        }
    }

    complete_apps = ['book']
