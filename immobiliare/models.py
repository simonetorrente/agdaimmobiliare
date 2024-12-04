from django.db import models

# Create your models here.

class Agenti(models.Model):
    cf = models.CharField(max_length=16, primary_key=True)
    email = models.EmailField(max_length=100)
    telefono = models.CharField(max_length=15)
    citta = models.CharField(max_length=255)
    via = models.CharField(max_length=255)
    civico = models.CharField(max_length=30)
    data_nascita = models.DateField()
    data_assunzione = models.DateField()
    stipendio = models.DecimalField(max_digits=10, decimal_places=2)
    trattative_concluse = models.IntegerField()

    class Meta:
        managed = True  
        db_table = 'agenti'  

    def __str__(self):
        return self.cf

class Appuntamenti(models.Model):
    id = models.IntegerField(primary_key=True)
    data_appuntamento = models.DateField(null=False)
    cliente = models.CharField(max_length=255, null=False)
    immobile = models.IntegerField(null=False)
    ora_appuntamento = models.TimeField(null=False)

    class Meta:
        managed = True  
        db_table = 'appuntamenti'  

    def __str__(self):
        return self.id

class Clienti(models.Model):
    email = models.CharField(max_length=255, primary_key=True)
    password_hash = models.CharField(max_length=255, null=False)
    telefono1 = models.CharField(max_length=255, null=True)
    telefono2 = models.CharField(max_length=255, null=True)
    ultimo_immobile_visto = models.IntegerField(null=True)
    nome = models.CharField(max_length=255, null=True)

    class Meta:
        managed = True 
        db_table = 'clienti' 

    def __str__(self):
        return self.email
    
class Proprietari(models.Model):
    cf = models.CharField(max_length=16, primary_key=True)
    email = models.CharField(max_length=100, null=True)
    telefono = models.CharField(max_length=15, null=True)
    nome = models.CharField(max_length=255, null=True)

    class Meta:
        managed = True  
        db_table = 'proprietari'  
    def __str__(self):
        return self.cf
    

class Immobili(models.Model):
    IN_VENDITA = "In vendita"
    IN_AFFITTO = "In affitto"
    VENDUTO = "Venduto"
    AFFITTATO = "Affittato"
    NON_DISPONIBILE = "Non disponibile"
    scelteSituazione = {
        IN_VENDITA: "In vendita",
        IN_AFFITTO: "In affitto",
        VENDUTO: "Venduto",
        AFFITTATO: "Affittato",
        NON_DISPONIBILE: "Non disponibile",

    }
    CASA_INDIPENDENTE = "Casa indipendente"
    APPARTAMENTO = "Appartamento"
    RUSTICO = "Rustico"
    ALTRO = "Altro"
    scelteTipo = {
        CASA_INDIPENDENTE: "Casa indipendente",
        APPARTAMENTO: "Appartamento",
        RUSTICO: "Rustico",
        ALTRO: "Altro",

    }
    riferimento = models.IntegerField(primary_key=True)
    situazione = models.CharField(max_length=100, choices=scelteSituazione, default=IN_VENDITA)
    prezzo = models.IntegerField()
    metratura = models.IntegerField()
    stato = models.CharField(max_length=255)
    citta = models.CharField(max_length=255)
    via = models.CharField(max_length=255)
    civico = models.CharField(max_length=30)
    tipo = models.CharField(max_length=100, choices=scelteTipo, default=CASA_INDIPENDENTE)
    descrizione = models.CharField(max_length=10000)
    spese_amministrazione = models.FloatField(null=True)
    spese_riscaldamento = models.FloatField(null=True)
    foto = models.ImageField(upload_to='immobili/', null=True, blank=True)
    video = models.FileField(upload_to='immobili/', null=True, blank=True)
    fasce_visite = models.CharField(max_length=255, null=True, blank=True)
    agente = models.ForeignKey(Agenti,on_delete=models.CASCADE, null=True, db_column='agente')
    proprietario = models.ForeignKey(Proprietari, on_delete=models.CASCADE, null=True, db_column='proprietario')

    class Meta:
        managed = True  
        db_table = 'immobili'  
    
    def __int__(self):
        return self.riferimento
    

class Foto(models.Model):
    immobile = models.ForeignKey(
        Immobili, 
        on_delete=models.CASCADE, 
        db_column='immobile',
        related_name='immagini'
    )
    IMG = "img"
    VIDEO = "video"   
    tipo_media = {
        IMG: "img",
        VIDEO: "video",
    }
    nome = models.CharField(max_length=255)
    file_path = models.URLField(max_length=255)
    descrizione = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"Foto di {self.immobile.riferimento} ({self.url_foto})"


