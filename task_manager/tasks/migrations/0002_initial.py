from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tasks', '0001_initial'),
        ('statuses', '0001_initial'),
        ('labels', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='author', to=settings.AUTH_USER_MODEL, verbose_name='Author'),
        ),
        migrations.AddField(
            model_name='task',
            name='executor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='executor', to=settings.AUTH_USER_MODEL, verbose_name='Executor'),
        ),
        migrations.AddField(
            model_name='task',
            name='labels',
            field=models.ManyToManyField(blank=True, related_name='labels', through='tasks.TaskLabelRelation', to='labels.label', verbose_name='labels'),
        ),
        migrations.AddField(
            model_name='task',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='statuses', to='statuses.status', verbose_name='Status'),
        ),
    ]