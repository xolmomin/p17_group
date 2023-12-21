from django.contrib import admin
from django.forms import forms
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import path
import csv
import io

from apps.models import Post, Comment, Category, Product


class CsvImportForm(forms.Form):
    csv_file = forms.FileField()


class ExportCsvMixin:
    def export_as_csv(self, request, queryset):
        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])

        return response

    export_as_csv.short_description = "Export Selected"


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin, ExportCsvMixin):
    change_list_template = "admin/change_list.html"

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('import-csv/', self.import_csv),
        ]
        return my_urls + urls

    def import_csv(self, request):
        if request.method == "POST":
            csv_file = request.FILES["csv_file"]
            reader = csv.reader(csv_file)
            for row in reader:
                print(row)
            self.message_user(request, "Your csv file has been imported")
            return redirect("..")
        form = CsvImportForm()
        payload = {"form": form}
        return render(request, "apps/csv_form.html", payload)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin, ExportCsvMixin):
    change_list_template = "admin/change_list.html"
    list_display = ['id', 'custom_title']

    def custom_title(self, obj):
        return ' '.join(obj.title.split()[:4])

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('import-csv/', self.import_csv),
        ]
        return my_urls + urls

    def import_csv(self, request):
        if request.method == "POST":
            csv_file = request.FILES["csv_file"]
            decoded_file = csv_file.read().decode('utf-8')
            io_string = io.StringIO(decoded_file)
            reader = csv.reader(io_string)
            next(reader)
            # v1

            # for row in reader:
            #     Post.objects.create(
            #         user_id=int(row[0]),
            #         id=int(row[1]),
            #         title=row[2],
            #         body=row[3]
            #     )
            # v2
            result = []
            for row in reader:
                print(row)
                result.append(Post(
                    user_id=int(row[0]),
                    id=int(row[1]),
                    title=row[2],
                    body=row[3]
                ))
            Post.objects.bulk_create(result)

            self.message_user(request, "Your csv file has been imported")
            return redirect("..")
        form = CsvImportForm()
        payload = {"form": form}
        return render(request, "apps/csv_form.html", payload)

    custom_title.short_description = 'Sarlavha'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass
