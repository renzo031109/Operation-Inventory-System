from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from .middleware import get_current_user



class Location(models.Model):
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.location
    
    class Meta:
        ordering = ["location"]

    #Save data to upper case
    def save(self):
        self.location= self.location.upper()
        super(Location, self).save()


class Gender(models.Model):
    gender = models.CharField(max_length=200)

    def __str__(self):
        return self.gender
    
    class Meta:
        ordering = ["gender"]

    #Save data to upper case
    def save(self):
        self.gender= self.gender.upper()
        super(Gender, self).save()


class Company(models.Model):
    company = models.CharField(max_length=200)

    def __str__(self):
        return self.company
    
    class Meta:
        ordering = ["company"]

    #Save data to upper case
    def save(self):
        self.company= self.company.upper()
        super(Company, self).save()



class Illness(models.Model):
    illness = models.CharField(max_length=200)

    def __str__(self):
        return self.illness
    
    class Meta:
        ordering = ["illness"]
        verbose_name = "Chief of Complaint"

    #Save data to upper case
    def save(self):
        self.illness = self.illness.upper()
        super(Illness, self).save()


class AMR(models.Model):
    amr = models.CharField(max_length=200)

    def __str__(self):
        return self.amr
    
    class Meta:
        ordering = ["amr"]
        verbose_name = "Body System Affected"

    #Save data to upper case
    def save(self):
        self.amr = self.amr.upper()
        super(AMR, self).save()



class Demand(models.Model):
    demand = models.CharField(max_length=30)
    
    def __str__(self):
        return self.demand
    
    class Meta:
        ordering = ["demand"]

    #Save data to upper case
    def save(self):
        self.demand= self.demand.upper()
        super(Demand, self).save()


# This is for code reference + details
class MedCode(models.Model):
    code = models.CharField(max_length=200, null=True)
    medicine = models.CharField(max_length=200, null=True)
    quantity = models.IntegerField(null=True)
    clinic_date_added = models.DateTimeField(auto_now_add=True, null=True)
    critical = models.IntegerField(null=True)
    consumed = models.IntegerField(default=0, null=True)
    note = models.TextField(null=True, blank=True)
    user = models.CharField(max_length=200, null=True)
    demand = models.ForeignKey(Demand, on_delete=models.SET_NULL, null=True, blank=True)   
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True, blank=True) 


    def __str__(self):
        return self.code

    class Meta:
        ordering = ["code"]
        verbose_name = "Medicine"
    
    #Save data to upper case
    def save(self, *args, **kwargs):
        self.code = self.code.upper()
        self.medicine = self.medicine.upper()
        super(MedCode, self).save(*args, **kwargs)


# This is the base Medicine Table
class Medicine(models.Model): 
    medicine = models.CharField(max_length=200)
    quantity = models.IntegerField(null=True)
    clinic_date_added = models.DateTimeField(auto_now_add=True, null=True)
    critical = models.IntegerField(null=True)
    consumed = models.IntegerField(default=0, null=True)
    medcode = models.ForeignKey(MedCode, on_delete=models.SET_NULL, null=True, blank=True, related_name="medicines")
    demand = models.ForeignKey(Demand, on_delete=models.SET_NULL, null=True, blank=True)   
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True, blank=True) 


    def __str__(self):
        return str(self.medcode)
    
    class Meta:
        ordering = ["medicine"]
        verbose_name = "zDUPLICATE"

    #Save data to upper case
    def save(self, *args, **kwargs):
        self.medicine = self.medicine.upper()
        super(Medicine, self).save(*args, **kwargs)



class MedicineMovement(models.Model):
    code = models.CharField(max_length=200, null=True)
    medicine = models.CharField(max_length=200, null=True)
    quantity = models.IntegerField(null=True)
    clinic_date_added = models.DateTimeField(auto_now_add=True, null=True)
    note = models.TextField(null=True, blank=True)
    user = models.CharField(max_length=200, null=True)
    location = models.ForeignKey(Location, models.SET_NULL, null=True) 


    def __str__(self):
        return self.code

    class Meta:
        ordering = ["-clinic_date_added"]
    
    #Save data to upper case
    def save(self, *args, **kwargs):
        self.medicine = self.medicine.upper()
        super(MedicineMovement, self).save(*args, **kwargs)




class MedicalServiceGiven(models.Model):
    medical_given = models.CharField(max_length=100)

    def __str__(self):
        return self.medical_given
    
    class Meta:
        ordering = ["medical_given"]
        db_table = "clinic_medicalservicegiven"  # Explicitly set table name

    #Save data to upper case
    def save(self):
        self.medical_given= self.medical_given.upper()
        super(MedicalServiceGiven, self).save()



class Clinic_Record(models.Model):
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True, blank=True)
    employee_id = models.CharField(max_length=50, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    first_name = models.CharField(max_length=200, null=True, blank=True)
    last_name = models.CharField(max_length=200, null=True, blank=True)
    gender = models.ForeignKey(Gender, on_delete=models.SET_NULL, null=True, blank=True)
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True, blank=True)
    department = models.CharField(max_length=200, null=True, blank=True)
    illness = models.ForeignKey(Illness, on_delete=models.SET_NULL, null=True, blank=True)
    amr = models.ForeignKey(AMR, on_delete=models.SET_NULL, null=True, blank=True)
    medcode = models.ForeignKey(MedCode, on_delete=models.SET_NULL, null=True)
    medicine = models.CharField(max_length=200, null=True, blank=True)
    quantity = models.IntegerField(null=True)
    date_added = models.DateTimeField(auto_now_add=True, null=True)
    medical_given = models.ForeignKey(MedicalServiceGiven, on_delete=models.SET_NULL, null=True, blank=True)
    note = models.TextField(null=True, blank=True)


    def __str__(self):
        return self.employee_id
    

    class Meta:
        ordering = ["-date_added"]

    #Save data to upper case
    def save(self):
        self.last_name = self.last_name.upper()
        self.first_name = self.first_name.upper()
        self.department = self.department.upper()
        super(Clinic_Record, self).save()



#signal when row is deleted
#This will log the row deleted in Admin panel
@receiver(pre_delete, sender=MedCode)
def log_medicine_deletion(sender, instance, **kwargs):
    current_user = get_current_user()  # Get the current user from thread-local storage
    MedicineMovement.objects.create(
        code=instance.code,
        medicine=instance.medicine,
        quantity=instance.quantity,
        note="DELETED",
        user=current_user.username if current_user else "Unknown",  # Use the current user
        location=instance.location
    )

