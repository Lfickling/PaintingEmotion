def saliency(x_pos, y_pos):
    #probably needs it's own whole class since it's a complex series of equations
    return 

def mask(x_pos, y_pos, eq_type):
    #enumerate different mask equations
    return

def rfa(image_matrix, eq_type):
    sum_saliency = 0
    sum_saliency_x_mask = 0
    for x in image_matrix.length():
        for y in image_matrix[x].length():
            pixel_saliency = saliency(x,y)
            sum_saliency += pixel_saliency
            sum_saliency_x_mask += (pixel_saliency * mask(x,y,eq_type))
    return (sum_saliency_x_mask / sum_saliency)

def itten_color(image_matrix, eq_type):
    #various itten eqs
    # calculate standard deviation
    itten_color_scores = []
    return itten_color_scores

def emphasis(image_matrix):
    #do we need to do anything to the image first?

    #calculate itten color scores

    #figure out RFA of image based on mask eq type combine those different RFAs together somehow?

    #calulate emphasis by combinding itten and RFA
    emphasis_score = 0
    return emphasis_score 

