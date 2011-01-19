# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Project.modified'
        db.add_column('work_project', 'modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=datetime.datetime(2011, 1, 19, 11, 38, 26, 604000), blank=True), keep_default=False)

        # Adding field 'Project.created'
        db.add_column('work_project', 'created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.datetime(2011, 1, 19, 11, 38, 32, 707805), blank=True), keep_default=False)

        # Deleting field 'Photo.created'
        db.delete_column('work_photo', 'created')

        # Deleting field 'Photo.modified'
        db.delete_column('work_photo', 'modified')


    def backwards(self, orm):
        
        # Deleting field 'Project.modified'
        db.delete_column('work_project', 'modified')

        # Deleting field 'Project.created'
        db.delete_column('work_project', 'created')

        # Adding field 'Photo.created'
        db.add_column('work_photo', 'created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.datetime(2011, 1, 19, 11, 38, 46, 428233), blank=True), keep_default=False)

        # Adding field 'Photo.modified'
        db.add_column('work_photo', 'modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=datetime.datetime(2011, 1, 19, 11, 39, 1, 308247), blank=True), keep_default=False)


    models = {
        'work.photo': {
            'Meta': {'object_name': 'Photo'},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'photo_set'", 'to': "orm['work.Project']"})
        },
        'work.project': {
            'Meta': {'object_name': 'Project'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'order': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['work']
