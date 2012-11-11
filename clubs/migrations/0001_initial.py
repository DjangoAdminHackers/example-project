# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Club'
        db.create_table('clubs_club', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=512)),
        ))
        db.send_create_signal('clubs', ['Club'])

        # Adding model 'Member'
        db.create_table('clubs_member', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('fname', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('sname', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('club', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['clubs.Club'])),
        ))
        db.send_create_signal('clubs', ['Member'])


    def backwards(self, orm):
        # Deleting model 'Club'
        db.delete_table('clubs_club')

        # Deleting model 'Member'
        db.delete_table('clubs_member')


    models = {
        'clubs.club': {
            'Meta': {'object_name': 'Club'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '512'})
        },
        'clubs.member': {
            'Meta': {'object_name': 'Member'},
            'club': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['clubs.Club']"}),
            'fname': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sname': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['clubs']