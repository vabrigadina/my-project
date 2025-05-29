from django.db import models

class AboutMe(models.Model):
    full_name = models.CharField(max_length=200, default="Бригадина Валерия Александровна")
    photo = models.ImageField(upload_to='photos/', blank=True, null=True)
    email = models.EmailField(default="vabrigadina@edu.hse.ru")
    phone = models.CharField(max_length=20, default="8 999 555 32 32")
    resume = models.ImageField(upload_to='resumes/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name

class EducationalProgram(models.Model):
    name = models.CharField(max_length=200, default="Иностранные языки и межкультурная коммуникация")
    link = models.URLField(default="https://www.hse.ru/ba/lang/")
    what_i_study = models.TextField(default="Я углублённо изучаю два иностранных языка: английский и второй на выбор — в моём случае, это французский. Помимо языков, мы изучаем межкультурную коммуникацию, основы перевода, цифровые коммуникации, методику преподавания, а также русский как иностранный. Программа даёт возможность выбирать майноры и элективные курсы — это позволяет строить свою образовательную траекторию.")
    what_i_learn = models.TextField(default="К окончанию обучения я смогу свободно говорить на двух иностранных языках, переводить тексты и устную речь, преподавать языки, вести проекты в сфере международного взаимодействия и использовать цифровые инструменты в своей работе. У нас много практики, стажировок и проектов, поэтому я не просто изучаю теорию, но и применяю знания на деле.")
    benefits = models.TextField(default="Мне нравится, что здесь гибкая программа, есть англоязычный трек, возможность участвовать в международных обменах. Преподаватели — настоящие профессионалы, а атмосфера очень вдохновляющая. Мы участвуем в конференциях, встречах с работодателями, творческих и исследовательских проектах — это помогает расти как личностно, так и профессионально.")
    prospects = models.TextField(default="После окончания программы я могу работать переводчиком, преподавателем, специалистом по международным коммуникациям, в сфере маркетинга, HR, в международных компаниях, культурных организациях. Можно пойти в магистратуру, заняться наукой или работать за границей.")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Management(models.Model):
    academic_director_name = models.CharField(max_length=200, default="Боголепова Светлана Викторовна")
    academic_director_photo = models.ImageField(upload_to='management_photos/', blank=True, null=True)
    academic_director_email = models.EmailField(default="svbogolepova@hse.ru")
    program_manager_name = models.CharField(max_length=200, default="Симонова Елена Алексеевна")
    program_manager_photo = models.ImageField(upload_to='management_photos/', blank=True, null=True)
    program_manager_email = models.EmailField(default="eakochetkova@hse.ru")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.academic_director_name} & {self.program_manager_name}"

class Classmate(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='classmate_photos/', blank=True, null=True)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name