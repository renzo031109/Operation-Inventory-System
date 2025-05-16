from django.db import models


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


class Department(models.Model):
    department = models.CharField(max_length=200)

    def __str__(self):
        return self.department
    
    class Meta:
        ordering = ["department"]
        verbose_name = "Department/Client"

    #Save data to upper case
    def save(self):
        self.department= self.department.upper()
        super(Department, self).save()


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



class Medicine(models.Model):
    medicine = models.CharField(max_length=200)
    quantity = models.IntegerField()
    clinic_date_added = models.DateTimeField(auto_now_add=True, null=True)
    critical = models.IntegerField(null=True)
    demand = models.ForeignKey(Demand, on_delete=models.CASCADE, null=True, blank=True)
    consumed = models.IntegerField(default=0, null=True)



    def __str__(self):
        return self.medicine
    
    class Meta:
        ordering = ["medicine"]

    #Save data to upper case
    def save(self):
        self.medicine = self.medicine.upper()
        super(Medicine, self).save()



#Duplicate to allow dropdown option
class MedicineNew(models.Model):
    medicine = models.ForeignKey(Medicine, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(null=True)


    def __str__(self):
        return self.medicine
    
    class Meta:
        ordering = ["medicine"]

    #Save data to upper case
    def save(self):
        self.medicine = self.medicine.upper()
        super(Medicine, self).save()



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
    location = models.ForeignKey(Location, on_delete=models.CASCADE, null=True, blank=True)
    employee_id = models.CharField(max_length=50, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    first_name = models.CharField(max_length=200, null=True, blank=True)
    last_name = models.CharField(max_length=200, null=True, blank=True)
    gender = models.ForeignKey(Gender, on_delete=models.SET_NULL, null=True, blank=True)
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True, blank=True)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True)
    illness = models.ForeignKey(Illness, on_delete=models.CASCADE, null=True, blank=True)
    amr = models.ForeignKey(AMR, on_delete=models.CASCADE, null=True, blank=True)
    medicine = models.ForeignKey(Medicine, on_delete=models.SET_NULL, null=True)
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
        super(Clinic_Record, self).save()