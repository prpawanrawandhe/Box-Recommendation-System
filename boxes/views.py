from django.shortcuts import render,redirect
from .models import Box


def box_recommendation(request):
    result = None
    searched = False
    all_boxes = Box.objects.all()

    boxes = {}

    for box in all_boxes:
        boxes[box.name] = [box.length,box.width,box.height,box.max_weight,box.cost]
    # print(boxes)
    
    if all(request.POST.get(field) for field in ['length', 'width', 'height', 'weight']):

        length = float(request.POST.get('length'))
        width = float(request.POST.get('width'))
        height = float(request.POST.get('height'))
        weight = float(request.POST.get('weight'))


        # product = [10,15,20, 3]
        product = [length,width,height,weight]

        suitable_boxes = {}

        product_dimensions = sorted(product[:3])

        for box_name, box in boxes.items():

            box_dimensions = sorted(box[:3])

            if (all(p <= b for p, b in zip(product_dimensions, box_dimensions))
                    and product[3] <= box[3]):

                suitable_boxes[box_name] = box[4]

        if suitable_boxes:
            box_name, price = min(suitable_boxes.items(), key=lambda item: item[1])
            print(box_name, price)
            result = Box.objects.get(name=box_name)
            print(result)

        else:
            print("No suitable box found")
            result = None
            searched = True

    
    return render(request,"home.html",{"recommended_box":result,"searched": searched})

