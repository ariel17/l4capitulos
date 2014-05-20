# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Book.category'
        db.alter_column(u'book_book', 'category_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['book.Category'], null=True))

        # Changing field 'Book.status'
        db.alter_column(u'book_book', 'status_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['book.Status'], null=True))
        # Adding field 'Category.parent'
        db.add_column(u'book_category', 'parent',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['book.Category'], null=True),
                      keep_default=False)


    def backwards(self, orm):

        # Changing field 'Book.category'
        db.alter_column(u'book_book', 'category_id', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['book.Category']))

        # Changing field 'Book.status'
        db.alter_column(u'book_book', 'status_id', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['book.Status']))
        # Deleting field 'Category.parent'
        db.delete_column(u'book_category', 'parent_id')


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
        }
    }

    complete_apps = ['book']