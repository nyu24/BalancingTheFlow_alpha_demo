# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define p = Character("You", color= "#df059a")
define tv = Character("Television")
define f = Character("Friend", color= "#7605df")


# The game starts here.
#This will contain all variables
default bedroom_status = False
default count_drawer_Tfrontdoor = False
default count_drawer_Tfrontdoor2 = False
define current_room = 'start'
default fn_status = False
#inventory variables
default keys = False
default fn_counter = False
default fn_for = False
default e_counter = False
default e_for = False
default politician = False

label start:

    #Tutorial
    $ current_room = "start"
    if bedroom_status:
        scene bk_t_bedroom
        call screen bd_press
    else:
        scene bk_t_bedroom
        p "Waking up to the sound of the TV playing isn't an everyday occurence."
        p "But, as weird as it was. If not for the TV, I wouldn't have known about, THAT."
        play sound "audio/newsbroadcast.mp3"
        tv "BREAKING NEWS: The city council is holding a vote for the construction of the (river name) Dam. For the first time in years, us the people will have a choice on the matter."
        p "Oh."
        p "That river."
        scene bk_river
        play music "audio/naturemusic.mp3" fadein 1.0 volume 0.5
        p "I spent a lot of time there with everyone."
        p "Most of it was me just... Trying to get away from life by canoeing or hanging out with my friends."
        p "But now that life's gotten more and more busy, I haven't really had the time to head back there."
        p "Not to mention, everyone else has been too busy to go hangout."
        p "But... If that dam were to be built...."
        scene bk_river_rev
        p "The river from my memories would cease to exist."
        stop music fadeout 1.0
        scene bk_t_bedroom
        play sound "audio/phone_buzz.mp3"
        "Phone" "*bzt* *bzt*"
        p "My phone? Who could be calling at this time?"
        scene phonecall_pending
        p "My friend!"
        p "Could she be calling about the dam?"
        scene phonecall_accepted
        f "Yo! Did you see what was on the TV?"
        p "I did, what about it?"
        f "I can’t believe they are making a dam, we always use to go canoeing at the river!"
        p "Yeah.. But we haven't been there in a while."
        f "That doesn't mean that place isn't important anymore!"
        p "..."
        f "Listen. You know how you work for the government? Your choice matters! Maybe... Your vote will make a difference on the council\'s decision to build the dam or not."
        p "But I don't know enough about dams to know if they really should be built or not..."
        f "Well my friend. You can learn."
        f "Some first nation communities located close to the river are protesting. Why don't you go speak to some of them and learn about their perspectives on the situation?"
        p "You know what? That\'s a great idea! I'll head on over right now."
        scene bk_t_bedroom
        $ bedroom_status = True
        call screen bd_press

#Inventory system
label inventory_room:
    scene inventory_background
    #THESE NEED TO BE ADDED IN INSTANCE
    #$ fn_counter = True
    #$ fn_for = True
    #$ e_counter = True
    #$ e_for = True
    #$ politician = True
    call screen inventory_icon_room

screen inventory_icon_room:
    if keys:
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.75
            ypos 0.6835
            idle "house_key.png"
            hover "house_key_hover.png"
    if fn_counter:
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.25
            ypos 0.25
            idle "evidence5.png"
            hover "evidence5_hover.png"

    if fn_for:
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.5
            ypos 0.25
            idle "evidence4.png"
            hover "evidence4_hover.png"

    if e_counter:
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.75
            ypos 0.25
            idle "evidence3.png"
            hover "evidence3_hover.png"

    if e_for:
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.25
            ypos 0.683
            idle "evidence2.png"
            hover "evidence2_hover.png"

    if politician:
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.5
            ypos 0.683
            idle "evidence1.png"
            hover "evidence1_hover.png"

    imagebutton:
        xanchor 0.5
        yanchor 0.5
        xpos 0.5
        ypos 0.9
        idle "back_button.png"
        hover "back_button_hover.png"
        action Jump(current_room)
        
screen bd_press:
    #drawer
    imagebutton:
        xanchor 0.5
        yanchor 0.5
        xpos 0.6269
        ypos 0.6835
        idle "bd_drawer.png"
        hover "bd_drawer_hover.png"
        action [Hide("bd_press"), Jump("emptyBDS")]
    #door
    imagebutton:
        xanchor 0.5
        yanchor 0.5
        xpos 0.309
        ypos 0.41
        idle "bd_door.png"
        hover "bd_door_hover.png"
        action [Hide("bd_press"), Jump("thall")]
    #folder
    imagebutton:
        xanchor 0.5
        yanchor 0.5
        xpos 0.07
        ypos 0.15
        idle "inventory_icon.png"
        hover "inventory_icon_hover.png"
        action Jump("inventory_room")

label emptyBDS:
    p "Just some random trinkets."
    jump start

label thall:
    $ current_room = 'thall'
    scene t_hallway
    call screen thall_press

screen thall_press:
    #bedroom door
    imagebutton:
        xanchor 0.5
        yanchor 0.5
        xpos 0.911
        ypos 0.5
        idle "rightdoor.png"
        hover "rightdoor_hover.png"
        action Jump("start")
    #office door
    imagebutton:
        xanchor 0.5
        yanchor 0.5
        xpos 0.090
        ypos 0.5
        idle "leftdoor.png"
        hover "leftdoor_hover.png"
        action Jump("toffice")
    #kitchen door
    imagebutton:
        xanchor 0.5
        yanchor 0.5
        xpos 0.3498
        ypos 0.336
        idle "bd_door.png"
        hover "bd_door_hover.png"
        action Jump("tkitchen")
    #folder
    imagebutton:
        xanchor 0.5
        yanchor 0.5
        xpos 0.07
        ypos 0.15
        idle "inventory_icon.png"
        hover "inventory_icon_hover.png"
        action Jump("inventory_room")

label toffice:
    $ current_room = 'toffice'
    scene t_office
    call screen toffice_press

screen toffice_press:
    #hallway door
    imagebutton:
        xanchor 0.5
        yanchor 0.5
        xpos 0.911
        ypos 0.5
        idle "rightdoor.png"
        hover "rightdoor_hover.png"
        action Jump("thall")
    #office drawer
    imagebutton:
        xanchor 0.5
        yanchor 0.5
        xpos 0.106
        ypos 0.811
        idle "officedrawer.png"
        hover "officedrawer_hover.png"
        action Jump("keydrawer")
    #office desk
    imagebutton:
        xanchor 0.5
        yanchor 0.5
        xpos 0.5
        ypos 0.581
        idle "toffice_desk.png"
        hover "toffice_desk_hover.png"
        action Jump("emptyTOD")
    #folder
    imagebutton:
        xanchor 0.5
        yanchor 0.5
        xpos 0.07
        ypos 0.15
        idle "inventory_icon.png"
        hover "inventory_icon_hover.png"
        action Jump("inventory_room")

label keydrawer:
    if keys:
        p "Just some stationary left."
    else:
        p "Oh! My keys, I'll need to this to leave."
        $ keys = True
    jump toffice

label emptyTOD:
    p "Old works papers... Old homework... Old everything..."
    jump toffice

label tkitchen:
    $ current_room = 'tkitchen'
    scene t_kitchen
    call screen tkitchen_press

screen tkitchen_press:
    #frontroom door
    imagebutton:
        xanchor 0.5
        yanchor 0.5
        xpos 0.911
        ypos 0.5
        idle "rightdoor.png"
        hover "rightdoor_hover.png"
        action Jump("tfrontroom")
    #hallway
    imagebutton:
        xanchor 0.5
        yanchor 0.5
        xpos 0.25
        ypos 0.86
        idle "arrowd.png"
        hover "arrowd_hover.png"
        action Jump("thall")
    #folder
    imagebutton:
        xanchor 0.5
        yanchor 0.5
        xpos 0.07
        ypos 0.15
        idle "inventory_icon.png"
        hover "inventory_icon_hover.png"
        action Jump("inventory_room")

label tfrontroom:
    $ current_room = 'tfrontroom'
    scene t_frontdoor
    call screen tfrontdoor_press

screen tfrontdoor_press:
    #end tutorial door
    imagebutton:
        xanchor 0.5
        yanchor 0.5
        xpos 0.349
        ypos 0.34
        idle "tfd_door.png"
        hover "tfd_door_hover.png"
        action Jump("check_keys")
    #kitchen
    imagebutton:
        xanchor 0.5
        yanchor 0.5
        xpos 0.090
        ypos 0.5
        idle "leftdoor.png"
        hover "leftdoor_hover.png"
        action Jump("tkitchen")
    #drawer
    imagebutton:
        xanchor 0.5
        yanchor 0.5
        xpos 0.638
        ypos 0.585
        idle "tfrontdrawer.png"
        hover "tfrontdrawer_hover.png"
        action Jump("tfrontdrawerlines")
    #folder
    imagebutton:
        xanchor 0.5
        yanchor 0.5
        xpos 0.07
        ypos 0.15
        idle "inventory_icon.png"
        hover "inventory_icon_hover.png"
        action Jump("inventory_room")

label tfrontdrawerlines:
    if count_drawer_Tfrontdoor2:
        p "Maybe my keys somewhere else in the house."
        jump tfrontroom
    elif count_drawer_Tfrontdoor:
        p "Oh my gosh!"
        p "Keys still arent in here."
        $ count_drawer_Tfrontdoor2 = True
        jump tfrontroom
    else:
        p "Keys aren't in here..."
        p "Where on earth did I put them?"
        $ count_drawer_Tfrontdoor = True
        jump tfrontroom

label check_keys:
    if keys:
        p "Onward!"
        jump map

    else:
        p "I can't leave without my keys!"
        p "I mean how else would I lock the door?"
        jump tfrontroom

#MAP SECTION STARTS HERE
label map:
    $ current_room = 'map'
    scene map_background
    p "Right, let's head to the neighborhood first to find more about how the dam affects people."
    call screen map_fn
    jump fn_room

screen map_fn:
    #neighborhood
    imagebutton:
        xanchor 0.5
        yanchor 0.5
        xpos 0.27
        ypos 0.185
        idle "map_neighborhood.png"
        hover "map_neighborhood_hover.png"
        action Jump("fn_room")

#NEIGHBORHOOD
label fn_room:
    $ current_room = "fn_room"
    if fn_status:
        scene fn_bksr
        p "Am I ready to leave this area?"
        menu:
            "Yep!":
                jump map_en
            "Still something to do.":
                jump choicesfnstay
    else:
        scene fn_bksr
        p "If I walk around I might run into some people to talk to."
        $ fn_status = True
        call screen fnsr_options

label choicesfnstay:
    $ current_room = "choicesfnstay"
    scene fn_bksr
    call screen fnsr_options

screen fnsr_options:
    #left option
    imagebutton:
        xanchor 0.5
        yanchor 0.5
        xpos 0.1
        ypos 0.6
        idle "arrowl.png"
        hover "arrowl_hover.png"
        action Jump("fnl")
    #right option
    imagebutton:
        xanchor 0.5
        yanchor 0.5
        xpos 0.9
        ypos 0.6
        idle "arrowr.png"
        hover "arrowr_hover.png"
        action Jump("fnr")    
    #folder
    imagebutton:
        xanchor 0.5
        yanchor 0.5
        xpos 0.07
        ypos 0.15
        idle "inventory_icon.png"
        hover "inventory_icon_hover.png"
        action Jump("inventory_room")

define fna = Character("Elder", color= "#12a683")
default been_fnl = False
default been_fnr = False

#LEFT ROOM
label fnl:
    if been_fnl:
        scene fn_bkl
        $ current_room = "fnl"
        call screen fnl_options

    else:
        scene fn_bkl
        $ current_room = "fnl"
        $ been_fnl = True
        show temp_npc
        p "Hi, I wanted to ask you some questions about the upcoming dam construction vote."
        fna "Of course, what is your question?"
        p "I would like to understand more about what you're advocating for. Could you tell me your opinion on the matter and why it's important to you?"
        fna "For one, I am completely against the whole dam construction idea."
        fna "Our ancestors have lived here for thousands of years. The nearby river is our lifeblood. It is not just water; it is our spirit, our heritage."
        fna "For some, these dams are progress. But to me, they are a means of destruction. They drown our lands, erasing our history and our future."
        menu: 
            "But doesn't powering our society with diesel fuel cause even more harm?":
                jump choicefnl1
            "So, the land provides for you and your community, and in turn you wish to protect it?":
                jump choicefnl2

label choicefnl1:
    fna "While that may be true, the consequences of building a dam are more harmful to my community."
    fna "You see, we lose more than just land; we lose a part of our identity. We lose our the areas where we hunt for food, for fish and deer. The result of the dam would cause flooding in our area, destroying vegetation, stripping the land of its natural resources."
    jump fnl_choice2
label choicefnl2:
    fna "Yes, this is the duty my community has held since the beginning. The land provides for us, we protect it in turn. Besides we use these lands as a means to provide for ourselves."
    jump fnl_choice2

label fnl_choice2:
    menu:
        "But, there's always a different place where you can hunt... With the amount of energy required for society, don't you think we need more dams to help foster this need?":
            jump choicefnl3
        "So, for you, you're generally against this as it is harmful for your community's existence and because it harms your identity?":
            jump choicefnl4

label choicefnl3:
    fna "It seems that you aren't listening to what I have to say."
    fna "Then, I will kindly ask you to leave me be."
    hide temp_npc
    p "That... could've gone better."
    p "I didn't get to ask her to add her account to my journal..."
    call screen fnl_options

label choicefnl4:
    fna "Yes."
    p "Would you be willing to write that down in my notebook for me? I wish to learn all that I can about this situation."
    fna "Of course!"
    $ fn_counter = True
    p "Thank you so much!"
    fna "Well I best go back to what I was doing before, take care."
    hide temp_npc
    call screen fnl_options

screen fnl_options:
    #right option
    imagebutton:
        xanchor 0.5
        yanchor 0.5
        xpos 0.9
        ypos 0.6
        idle "arrowr.png"
        hover "arrowr_hover.png"
        action Jump("fn_room")    
    #folder
    imagebutton:
        xanchor 0.5
        yanchor 0.5
        xpos 0.07
        ypos 0.15
        idle "inventory_icon.png"
        hover "inventory_icon_hover.png"
        action Jump("inventory_room")

#RIGHT ROOM
define fnf = Character("Community Member", color= "#54cd03")
label fnr:
    scene fn_bkr
    $ current_room = "fnr"
    if been_fnr:
        call screen fnr_options
    else:
        show fnafor
        #add dialogue later
        fnf "Oh, hello there! How can I help you?"
        p "The rest of this section is a WIP!"
        if been_fnl:
            p "Since you've been to the left area, feel free to leave the neighborhood for the ending message :)"
            call screen fnr_options
        else:
            p "How about you check out the left area?"
            call screen fnr_options


screen fnr_options:
    #left option
    imagebutton:
        xanchor 0.5
        yanchor 0.5
        xpos 0.1
        ypos 0.6
        idle "arrowl.png"
        hover "arrowl_hover.png"
        action Jump("fn_room")
    #folder
    imagebutton:
        xanchor 0.5
        yanchor 0.5
        xpos 0.07
        ypos 0.15
        idle "inventory_icon.png"
        hover "inventory_icon_hover.png"
        action Jump("inventory_room")




label map_en:
    #To change later in the final/beta version
    scene map_background
    p "That's everything that alpha has to offer!"
    p "Merci beaucoup pour jouer notre jeu video! :)"
    jump end


label end:
    return
