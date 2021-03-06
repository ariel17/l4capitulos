# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Book.editorial'
        db.delete_column(u'book_book', 'editorial')


    def backwards(self, orm):
        # Adding field 'Book.editorial'
        db.add_column(u'book_book', 'editorial',
                      self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True),
                      keep_default=False)


    models = {
        u'book.author': {
            'Meta': {'ordering': "['first_name', 'last_name']", 'unique_together': "(('first_name', 'last_name'),)", 'object_name': 'Author'},
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'book.availability': {
            'Meta': {'object_name': 'Availability'},
            'book': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['book.Book']", 'unique': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'quantity': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'})
        },
        u'book.book': {
            'Meta': {'ordering': "['title']", 'object_name': 'Book'},
            'added_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'authors': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['book.Author']", 'null': 'True', 'blank': 'True'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['book.Category']", 'null': 'True', 'blank': 'True'}),
            'editorial_fk': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['book.Editorial']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'isbn': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'published_at': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
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