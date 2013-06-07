from django.http import HttpResponse, HttpRequest
from functools import wraps
import simplejson as json
from django.core import serializers
from backend.models import CV, Profile, Education, Experience, Courses


def render_to_json(**jsonargs):
    """
    Renders a JSON response with a given returned instance. Assumes json.dumps() can
    handle the result. The default output uses an indent of 4.
    
    @render_to_json()
    def a_view(request, arg1, argN):
        ...
        return {'x': range(4)}

    @render_to_json(indent=2)
    def a_view2(request):
        ...
        return [1, 2, 3]

    """
    def outer(f):
        @wraps(f)
        def inner_json(request, *args, **kwargs):
            result = f(request, *args, **kwargs)
            r = HttpResponse(mimetype='application/json')
            if result:
                indent = jsonargs.pop('indent', 4)
                r.write(json.dumps(result, indent=indent, **jsonargs))
            else:
                r.write("{}")
            return r
        return inner_json
    return outer


@render_to_json()
def index(request):
	
	cvs = CV.objects.all()


	for cv in cvs:
		data = {}
		# data['container'] = cv.container

		data['title'] = "Cargar Hoja de vida"

		sections_array = []
		

		i=0

		while(i<4):
			sections_elements = {}
			if(i==0):
				print("entro 0")
				sections_elements['header'] = "Profile"

				elements_array = []
				element_objects = {}


				element_objects['type'] = "root"
				element_objects['title'] = "Perfil"
				elements_array.append(element_objects)
				profiles = Profile.objects.filter(cv=cv.pk)


				inner_section_array = []
				inner_section_object = {}

				inner_section_object['header'] = profiles[0].summary
				# inner_section_object['caption'] = profile.summary
				inner_section_array.append(inner_section_object)

				inner_element_array = []
				
				# for profile in profiles:
				# 	inner_elements_object = {}
					
				# 	inner_elements_object['type'] = "string"
				# 	inner_elements_object['caption'] = profile.summary
				# 	inner_element_array.append(inner_elements_object)
					

				inner_section_object['elements'] = inner_element_array

				element_objects['sections']= inner_section_array

				sections_elements['elements'] = elements_array

				sections_array.append(sections_elements)


			if(i==1):
				print("entro 1")
				sections_elements['header'] = "Education"


				educations = Education.objects.filter(cv=cv.pk)
				elements_array = []
				
				

				for education in educations:
					element_objects = {}

					element_objects['type'] = "root"
					element_objects['title'] = education.degree
					elements_array.append(element_objects)



					inner_section_array = []
					inner_section_object = {}

					inner_section_object['header'] = education.degree
					inner_section_array.append(inner_section_object)


					inner_element_array = []

					inner_elements_object = {}
					
					inner_elements_object['type'] = "string"
					inner_elements_object['caption'] = education.institution
					inner_element_array.append(inner_elements_object)

					inner_elements_object1= {}

					inner_elements_object1['type'] = "string"
					inner_elements_object1['caption'] = education.city
					inner_element_array.append(inner_elements_object1)


					inner_elements_object2= {}

					inner_elements_object2['type'] = "string"
					inner_elements_object2['caption'] = education.year
					inner_element_array.append(inner_elements_object2)


					inner_section_object['elements'] = inner_element_array


					element_objects['sections'] = inner_section_array





				sections_elements['elements'] = elements_array

				sections_array.append(sections_elements)

			if(i==2):

				sections_elements['header'] = "Experience"


				experiences = Experience.objects.filter(cv=cv.pk)
				elements_array = []
				
				

				for experience in experiences:
					element_objects = {}

					element_objects['type'] = "root"
					element_objects['title'] = experience.job_title
					elements_array.append(element_objects)



					inner_section_array = []
					inner_section_object = {}

					inner_section_object['header'] = experience.job_title
					inner_section_array.append(inner_section_object)


					inner_element_array = []

					inner_elements_object = {}
					
					inner_elements_object['type'] = "string"
					inner_elements_object['caption'] = experience.institution
					inner_element_array.append(inner_elements_object)

					
					# Pilas hay que arreglar los atributos de las fechas


					inner_elements_object1= {}

					inner_elements_object1['type'] = "string"


					inner_elements_object1['caption'] = experience.start_date.strftime('%Y/%m/%d')
					inner_element_array.append(inner_elements_object1)


					inner_elements_object2= {}

					inner_elements_object2['type'] = "string"
					inner_elements_object2['caption'] = experience.end_date.strftime('%Y/%m/%d')
					inner_element_array.append(inner_elements_object2)


					inner_section_object['elements'] = inner_element_array

					element_objects['sections'] = inner_section_array





				sections_elements['elements'] = elements_array

				sections_array.append(sections_elements)



			if(i==3):

				sections_elements['header'] = "Courses"


				courses = Courses.objects.filter(cv=cv.pk)
				elements_array = []
				
				

				for course in courses:
					element_objects = {}

					element_objects['type'] = "root"
					element_objects['title'] = course.course_title
					elements_array.append(element_objects)



					inner_section_array = []
					inner_section_object = {}

					inner_section_object['header'] = course.course_title
					inner_section_array.append(inner_section_object)


					inner_element_array = []

					inner_elements_object = {}
					
					inner_elements_object['type'] = "string"
					inner_elements_object['caption'] = course.institution
					inner_element_array.append(inner_elements_object)

					inner_elements_object1= {}

					inner_elements_object1['type'] = "string"
					inner_elements_object1['caption'] = course.city
					inner_element_array.append(inner_elements_object1)

					# convertir a string el date


					inner_elements_object2= {}

					inner_elements_object2['type'] = "string"
					inner_elements_object2['caption'] = course.date.strftime('%Y/%m/%d')
					inner_element_array.append(inner_elements_object2)


					inner_section_object['elements'] = inner_element_array

					element_objects['sections'] = inner_section_array





				sections_elements['elements'] = elements_array

				sections_array.append(sections_elements)

			i+=1

		data['sections'] = sections_array


		return data
