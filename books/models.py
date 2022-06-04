from django.db import models

#Model Books
class Books(models.Model):
    id = models.AutoField(primary_key=True, db_column="id_books")
    nome = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    data_cadastro = models.DateField('Data de cadastro', auto_now_add=True)

    def __str__(self):
        return '{}'.format(self.nome)

    class Meta:
        db_table = "book"
        managed = True