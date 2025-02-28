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

    #Save data to upper case
    def save(self):
        self.amr = self.amr.upper()
        super(AMR, self).save()


class Medicine(models.Model):
    medicine = models.CharField(max_length=200)
    quantity = models.IntegerField()

    def __str__(self):
        return self.medicine
    
    class Meta:
        ordering = ["medicine"]

    #Save data to upper case
    def save(self):
        self.medicine = self.medicine.upper()
        super(Medicine, self).save()


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