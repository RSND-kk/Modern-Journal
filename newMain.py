from kivy.core.window import Window
from kivy.lang import Builder
from kivy.core import clipboard as clp
from kivy.properties import ObjectProperty, StringProperty, NumericProperty, Clock
from kivy.uix.behaviors import ButtonBehavior
from kivymd.app import MDApp
from kivymd.uix.behaviors import HoverBehavior
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDIconButton, MDFabButton
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.list import MDListItem
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.snackbar import MDSnackbar, MDSnackbarText
from kivymd.uix.gridlayout import MDGridLayout
from kivy.animation import Animation
from kivymd.uix.tooltip import MDTooltip
from kivymd.uix.transition import MDSlideTransition
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.list import MDList


from pyJournal import Database, Student


KV = """

WindowManager:
    SplashScreen
    MainScreen

<WindowManager@MDScreenManager>


<MenuHeader>
    spacing: "12dp"
    padding: "4dp"
    adaptive_height: True

    MDIconButton:
        icon: "gesture-tap-button"
        pos_hint: {"center_y": .5}

    MDLabel:
        text: "Actions"
        adaptive_size: True
        pos_hint: {"center_y": .5}
        
        
<MyTooltip@MDTooltip>:
    MDTooltipRich:
        auto_dismiss: True
        
        MDTooltipRichSubhead:
            text: root.txtTooltipHead
            
        MDTooltipRichSupportingText:
            text: root.txtTooltipBody     
            
            
<InstrumentPlace@MDGridLayout>:
    id: instrumentPlace
    cols: 7
    spacing: 5
    padding: 5
    size_hint: None, None
    size: "600dp", "70dp"
        
    InstrumentButton:
        icon: "check"
        value: "view"
        mainIcon: "eye-outline"
        posIcon: {"center_x": 0.3, "center_y": 0.5}
        posMainIcon: {"center_x": 0.7, "center_y": 0.5}
        
    InstrumentButton:
        value: "H1"
        mainIcon: "format-header-1"

    InstrumentButton:
        value: "1"
        mainIcon: "numeric-1-circle"

    InstrumentButton:
        value: "2"
        mainIcon: "numeric-2-circle"
    
    InstrumentButton:
        value: "3"
        mainIcon: "numeric-3-circle"
    
    InstrumentButton:
        value: "4"
        mainIcon: "numeric-4-circle"
    
    InstrumentButton:
        value: "5"
        mainIcon: "numeric-5-circle"
        
    InstrumentButton:
        value: "clear"
        mainIcon: "delete-circle"
        
    InstrumentButton:
        value: "H2"
        mainIcon: "format-header-2"
        
    InstrumentButton:
        value: "6"
        mainIcon: "numeric-6-circle"
        
    InstrumentButton:
        value: "7"
        mainIcon: "numeric-7-circle"
        
    InstrumentButton:
        value: "8"
        mainIcon: "numeric-8-circle"
        
    InstrumentButton:
        value: "9"
        mainIcon: "numeric-9-circle"
        
    InstrumentButton:
        value: "10"
        mainIcon: "numeric-10-circle"
        
    
<InstrumentButton@FloatLayout>:
    orientation: 'horizontal'
    value: root.value
    size_hint: None, None
    size: "80dp", "30dp"
    md_bg_color: [0, 0.4, 0, 0.3]
    radius: [10,]

    MDIcon:
        icon: root.icon
        padding: 10
        pos_hint: root.posIcon

    MDIcon:
        icon: root.mainIcon
        pos_hint: root.posMainIcon
        
        
<NavItem@MDIconButton>:
    icon: root.icon
    style: "standard"
    
    
<NavGroup@MDGridLayout>:
    id: root.id
    cols: root.cols
    adaptive_width: True
    spacing: 20
    padding: [20, 100, 20, 100]


<NavRail@MDFloatLayout>:
    orientation: 'vertical'
    md_bg_color: 0.85, 0.9, 0.8, 0.9
    size_hint_y: 1
    size_hint_x: None
    pos_hint_x: {"center_x": 0.5}
    width: "80dp"

    MDFabCustomButton:
        icon: "home"
        txtTooltipHead: "Home"
        txtTooltipBody: "Selection with hottest news, events and more."
        
        pos_hint: {"center_x": 0.5, "center_y": 0.9}
        on_release: app.homeClick(self)
                
        canvas.before:
            Color:
                rgba: 0.4, 0.6, 0.4, 1
            RoundedRectangle:
                pos: self.x - 2, self.y - 2
                size: self.width + 4, self.height + 4
                radius: [18,]
            Color:
                rgba: 0.4, 0.6, 0.4, 1
            RoundedRectangle:
                pos: self.pos
                size: self.size
                radius: [18,]

    NavItem:
        icon: "eye-outline"
        txtTooltipHead: "Viewing"
        txtTooltipBody:
            "In this section you can view students from different groups, set passes, grades and much more."
        width: "60dp"
        height: "60dp"
        pos_hint: {"center_x": 0.5, "center_y": 0.6}
        on_release: app.railClick(self, "viewGroupScreen")

    NavItem:
        icon: "account-group-outline"
        txtTooltipHead: "Management"
        txtTooltipBody:
            "In this section you can edit personal data of students, add new ones,\\n" \
             "delete expelled ones, edit, manage groups and more"
        width: "60dp"
        height: "60dp"
        pos_hint: {"center_x": 0.5, "center_y": 0.5}
        on_release: app.railClick(self, "changeGroup")

    NavItem:
        icon: "cog"
        txtTooltipHead: "Settings"
        txtTooltipBody:
            "In this section you can change application settings."
        width: "60dp"
        height: "60dp"
        pos_hint: {"center_x": 0.5, "center_y": 0.4}
        on_release: app.railClick(self, "settings")

    NavItem:
        icon: "help-circle-outline"
        txtTooltipHead: "Help"
        txtTooltipBody:
            "In this section you can find answers to frequently asked questions."
        width: "60dp"
        height: "60dp"
        pos_hint: {"center_x": 0.5, "center_y": 0.3}
        on_release: app.railClick(self, "help")


<ChangeGroupItem>:
    orientation: 'vertical'
    size_hint_x: None
    size_hint_y: None
    height: "400dp"
    width: "300dp"

    canvas.before:
        Color:
            rgba: 0, 0, 0, 0.1
        RoundedRectangle:
            pos: self.x - 4, self.y - 4
            size: self.width + 8, self.height + 8
            radius: [20,]
        Color:
            rgba: 0.85, 0.9, 0.8, 0.9
        RoundedRectangle:
            pos: self.pos
            size: self.size
            radius: [20,]

    MDBoxLayout:
        orientation: 'vertical'
        size_hint: 1, 0.9
        pos_hint: {"center_x": 0.5, "top": 1}

        FitImage:
            source: root.image
            size_hint: 1, 0.5
            pos_hint: {"center_x": 0.5, "top": 1}
            radius: [20, 20, 20, 20]

    MDBoxLayout:
        orientation: 'vertical'
        size_hint: 1, 0.1
        pos_hint: {"center_x": 0.5, "bottom": 1}

        MDLabel:
            text: root.text
            bold: True
            size_hint: 1, 1
            halign: 'center'


<MyButton@MDBoxLayout>:
    orientation: 'horizontal'
    md_bg_color: root.bgColor
    size_hint: None, None
    size: "120dp", "40dp"
    spacing: 10
    padding: 7
    radius: [20,]

    MDIcon:
        icon: root.icon
        size_hint: None, None
        size: "40dp", "40dp"

        pos_hint: {"left": 1, "center_y": 0.5}

        canvas.before:
            Color:
                rgba: 0, 0.4, 0, 0.3
            RoundedRectangle:
                pos: self.x - 7, self.y - 7
                size: self.width + 14, self.height + 14
                radius: [20,]
    
    MDLabel:
        font_size: root.fontSize
        font_name: root.fontName
        text: root.text
        bold: True
        valign: 'middle'
        pos_hint: {"x": 0.5, "center_y": 0.5}
        
        
<MyIconButton@MDBoxLayout>:
    orientation: 'horizontal'
    md_bg_color: root.bgColor
    size_hint: None, None
    size: "120dp", "40dp"
    spacing: 10
    padding: 15
    radius: [18,]

    canvas.before:
        Color:
            rgba: 0, 0, 0, 0.05
        RoundedRectangle:
            pos: self.x - 1, self.y - 1
            size: self.width + 2, self.height + 2
            radius: [20,]

    MDIcon:
        icon: root.icon
        size_hint: None, None
        size: "40dp", "40dp"
        pos_hint: {"left": 1, "center_y": 0.5}
    
    MDLabel:
        font_size: root.fontSize
        font_name: root.fontName
        text: root.text
        bold: True
        valign: 'middle'
        pos_hint: {"x": 0.5, "center_y": 0.5}
                  
<HomeWidgetInfo@MDBoxLayout>
    orientation: 'vertical'
    size_hint: None, None
    width: root.width
    height: root.height
    
    canvas.before:
        Color:
            rgba: 0, 0, 0, 0.1
        RoundedRectangle:
            pos: self.pos
            size: self.size
            radius: [20,]
    
    MDBoxLayout:
        orientation: 'vertical'
        size_hint: 1, 1
        padding: "10dp"
        spacing: "10dp"
        
        MDLabel:
            text: root.text
            bold: True
            size_hint: 1, 0.1
            halign: 'center'
            pos_hint: {"center_y": 0.9}
            
        MDBoxLayout:
            orientation: 'vertical'
            size_hint: 0.99, 0.8
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            canvas.before:
                Color:
                    rgba: 0, 0, 0, 0.08
                RoundedRectangle:
                    pos: self.pos
                    size: self.size
                    radius: [20,]
            
            MDLabel:
                text: root.infoOfWidget
                size_hint: 1, 1
                pos_hint: {"center_x": 0.5, "center_y": 0.5}
                halign: 'center'
                valign: 'center'
                font_size: 15
                
                
<SettingsWidgetInfo@MDBoxLayout>
    orientation: 'vertical'
    size_hint: None, None
    width: root.width
    height: root.height

    canvas.before:
        Color:
            rgba: 0, 0, 0, 0.1
        RoundedRectangle:
            pos: self.pos
            size: self.size
            radius: [20,]

    MDBoxLayout:
        orientation: 'vertical'
        size_hint: 1, 1
        padding: "10dp"
        spacing: "10dp"

        MDLabel:
            text: "Table Configuration"
            bold: True
            size_hint: 1, 0.1
            halign: 'center'
            pos_hint: {"center_y": 0.9}

        MDBoxLayout:
            orientation: 'vertical'
            size_hint: 0.99, 0.8
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            canvas.before:
                Color:
                    rgba: 0, 0, 0, 0.08
                RoundedRectangle:
                    pos: self.pos
                    size: self.size
                    radius: [20,]

            MDGridLayout:
                cols: 2
                size_hint: 1, 1
                pos_hint: {"center_x": 0.5, "center_y": 0.5}
                spacing: "10dp"
                
                MDBoxLayout:
                    orientation: "vertical"
                    size_hint: None, None
                    size: "48dp", "48dp"
                    pos_hint: {"center_x": 0.5, "center_y": 0.5}
                    padding: "10dp"
            
                    MDCheckbox:
                        group: "version"
                        size_hint: None, None
                        size: "48dp", "48dp"
                        pos_hint: {"center_x": 0.5, "center_y": 0.5}
            
                MDLabel:
                    text: "Old Version(In Progress)"
                    halign: "center"
                    bold: True
                    
                MDBoxLayout:
                    orientation: "vertical"
                    size_hint: None, None
                    size: "48dp", "48dp"
                    pos_hint: {"center_x": 0.5, "center_y": 0.5}
                    padding: "10dp"
            
                    MDCheckbox:
                        group: "version"
                        active: True
                        size_hint: None, None
                        size: "48dp", "48dp"
                        pos_hint: {"center_x": 0.5, "center_y": 0.5}
            
                MDLabel:
                    text: "Smart UI"
                    halign: "center"
                    bold: True
                    
                
<HelpWidgetPrg@MDBoxLayout>
    orientation: 'vertical'
    size_hint: None, None
    width: root.width
    height: root.height

    canvas.before:
        Color:
            rgba: 0, 0, 0, 0.1
        RoundedRectangle:
            pos: self.pos
            size: self.size
            radius: [20,]

    MDBoxLayout:
        orientation: 'vertical'
        size_hint: 1, 1
        padding: "10dp"
        spacing: "10dp"

        MDLabel:
            text: "About Program"
            bold: True
            size_hint: 1, 0.1
            halign: 'center'
            pos_hint: {"center_y": 0.9}

        MDBoxLayout:
            orientation: 'vertical'
            size_hint: 0.99, 0.8
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            canvas.before:
                Color:
                    rgba: 0, 0, 0, 0.08
                RoundedRectangle:
                    pos: self.pos
                    size: self.size
                    radius: [20,]
                    
            MDBoxLayout:
                orientation: 'vertical'
                size_hint: 1, 1
                padding: "10dp"
                spacing: "10dp"
                
                MDLabel:
                    text: 
                        '''The "Modern Journal" program is an application for recording students' attendance and academic performance in laboratory classes.
                        It is intended for teachers, providing a convenient interface for monitoring and analyzing academic performance. The system has the following capabilities:
                
                        - Registration of students and their grades.
                        - Accounting for attendance by subject.
                        - Viewing and editing data on students and groups.
                        - Managing academic workloads and schedules.
                        - Visualization of data in the form of tables to simplify analysis.
                            
                        The program has a convenient and intuitive interface, made using current technologies and standards.'''
                    halign: "center"
                    valign: "middle"
                    bold: True
                    pos_hint: {"center_x": 0.5, "center_y": 0.5}


<HelpWidgetAuthor@MDBoxLayout>
    orientation: 'vertical'
    size_hint: None, None
    width: root.width
    height: root.height

    canvas.before:
        Color:
            rgba: 0, 0, 0, 0.1
        RoundedRectangle:
            pos: self.pos
            size: self.size
            radius: [20,]

    MDBoxLayout:
        orientation: 'vertical'
        size_hint: 1, 1
        padding: "10dp"
        spacing: "10dp"

        MDLabel:
            text: "About Author"
            bold: True
            size_hint: 1, 0.1
            halign: 'center'
            pos_hint: {"center_y": 0.9}

        MDBoxLayout:
            orientation: 'vertical'
            size_hint: 0.99, 0.8
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            canvas.before:
                Color:
                    rgba: 0, 0, 0, 0.08
                RoundedRectangle:
                    pos: self.pos
                    size: self.size
                    radius: [20,]
                    
            MDBoxLayout:
                orientation: 'vertical'
                size_hint: 1, 1
                padding: "10dp"
                spacing: "10dp"
                
                MDLabel:
                    text: "This application was developed by me,"
                    bold: True
            
                MDLabel:
                    text: ""
                    bold: True

                MDLabel:
                    text: "The project was implemented as part of the course on the subject 'Programming Languages' and is designed to simplify the accounting of students' attendance and academic performance in laboratory classes."
                    bold: True
            
                MDLabel:
                    text: "The program includes functions for registering students, accounting for their attendance and grades, as well as analyzing data in the form of tables."
                    bold: True
            
                MDLabel:
                    text: "Contacts:"
                    bold: True
            
                MDLabel:
                    text: "E-mail: "
                    bold: True



<ColorSettingsWidgetInfo@MDBoxLayout>
    orientation: 'vertical'
    size_hint: None, None
    width: root.width
    height: root.height

    canvas.before:
        Color:
            rgba: 0, 0, 0, 0.1
        RoundedRectangle:
            pos: self.pos
            size: self.size
            radius: [20,]

    MDBoxLayout:
        orientation: 'vertical'
        size_hint: 1, 1
        padding: "10dp"
        spacing: "10dp"

        MDLabel:
            text: "Choose a Sheet Color Theme"
            bold: True
            size_hint: 1, 0.1
            halign: 'center'
            pos_hint: {"center_y": 0.9}

        MDBoxLayout:
            orientation: 'vertical'
            size_hint: 0.99, 0.8
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            canvas.before:
                Color:
                    rgba: 0, 0, 0, 0.08
                RoundedRectangle:
                    pos: self.pos
                    size: self.size
                    radius: [20,]

            MDGridLayout:
                cols: 1
                size_hint: 1, 1
                pos_hint: {"center_x": 0.5, "center_y": 0.5}
                spacing: "10dp"
                padding: "35dp"

                MyIconButton:
                    icon: "palette"
                    text: "Red"
                    pos_hint: {"center_x": 0.5}
                    on_release: app.changeTheme("Red")

                MyIconButton:
                    icon: "palette"
                    text: "Green"
                    pos_hint: {"center_x": 0.5}
                    on_release: app.changeTheme("Green")

                MyIconButton:
                    icon: "palette"
                    text: "Blue"
                    pos_hint: {"center_x": 0.5}
                    on_release: app.changeTheme("Blue")
                    
                    
<ModeSettingsWidgetInfo@MDBoxLayout>
    orientation: 'vertical'
    size_hint: None, None
    width: root.width
    height: root.height

    canvas.before:
        Color:
            rgba: 0, 0, 0, 0.1
        RoundedRectangle:
            pos: self.pos
            size: self.size
            radius: [20,]

    MDBoxLayout:
        orientation: 'vertical'
        size_hint: 1, 1
        padding: "10dp"
        spacing: "10dp"

        MDLabel:
            text: "Choose App Appearance Mode"
            bold: True
            size_hint: 1, 0.1
            halign: 'center'
            pos_hint: {"center_y": 0.9}

        MDBoxLayout:
            orientation: 'vertical'
            size_hint: 0.99, 0.8
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            canvas.before:
                Color:
                    rgba: 0, 0, 0, 0.08
                RoundedRectangle:
                    pos: self.pos
                    size: self.size
                    radius: [20,]

            MDGridLayout:
                cols: 1
                size_hint: 1, 1
                pos_hint: {"center_x": 0.5, "center_y": 0.5}
                spacing: "10dp"
                padding: "35dp"

                MyIconButton:
                    icon: "invert-colors"
                    text: "Light"
                    pos_hint: {"center_x": 0.5}
                    on_release: app.changeThemeMode("Light")

                MyIconButton:
                    icon: "invert-colors"
                    text: "Dark"
                    pos_hint: {"center_x": 0.5}
                    on_release: app.changeThemeMode("Dark")


<StudentInfoWidget@MDListItem>:
    pos_hint_y: 0.5
    size_hint: 1, 0.1
    radius: 20

    MDListItemLeadingIcon:
        icon: root.icon

    MDListItemHeadlineText:
        text: root.text

<StudentInfoLayout@MDBoxLayout>:
    orientation: 'vertical'
    size_hint: 0.3, 1
    elevation: 10
    padding: "10dp"
    spacing: "10dp"
    md_bg_color: 0.0, 0.5, 0.0, 0.08
    radius: 20

    MDLabel:
        pos_hint_y: 1
        size_hint: 1, 0.1
        text: "Student Information"
        halign: "center"
        bold: True

        canvas.before:
            Color:
                rgba: 0.0, 0.5, 0.0, 0.3
            RoundedRectangle:
                pos: self.pos
                size: self.size
                radius: [20, ]

    FitImage:
        source: "pictures/student.png"
        size_hint: 1, 0.3
        pos_hint_y: 0.8
        radius: [50, ]

    StudentInfoWidget:
        id: studentID
        icon: "identifier"
        text: "7"
        on_release: app.snackBarCopy(self.text)

    StudentInfoWidget:
        id: studentLastName
        icon: "account"
        text: "Clara"
        on_release: app.snackBarCopy(self.text)

    StudentInfoWidget:
        id: studentFirstName
        icon: "account"
        text: "Still"
        on_release: app.snackBarCopy(self.text)

    StudentInfoWidget:
        id: studentMiddleName
        icon: "account"
        text: "Ivanovna"
        on_release: app.snackBarCopy(self.text)

    StudentInfoWidget:
        id: studentPhone
        icon: "phone"
        text: "+375(29)123-45-67"
        on_release: app.snackBarCopy(self.text)

    StudentInfoWidget:
        id: studentEmail
        icon: "email"
        text: "claraStill@gmail.com"
        on_release: app.snackBarCopy(self.text)

    StudentInfoWidget:
        id: studentRating
        icon: "numeric-10-box-multiple"
        text: "7.3"
        on_release: app.snackBarCopy(self.text)

    StudentInfoWidget:
        id: studentMissing
        icon: "alpha-h-box"
        text: "4"
        on_release: app.snackBarCopy(self.text)


<CellStudentHead@MDBoxLayout>:
    size_hint: None, None
    width: "220dp"
    height: "48dp"
    halign: 'center'
    valign: 'middle'

    canvas.before:
        Color:
            rgba: [0.0, 0.5, 0.0, 0.3]
        RoundedRectangle:
            pos: self.pos
            size: self.size

    MDLabel:
        halign: 'center'
        valign: 'middle'
        bold: True
        text: root.text
        
<CellEditStudent@MDBoxLayout>:
    size_hint: None, None
    width: "220dp"
    height: "48dp"
    halign: 'center'
    valign: 'middle'

    canvas.before:
        Color:
            rgba: 0, 0, 0, 0.1
        Rectangle:
            pos: self.x - 2, self.y - 2
            size: self.width + 4, self.height + 4

    MDListItem:
        id: root.id
        on_release: app.showStudentEdit(root.id)
        MDListItemLeadingIcon:
            icon: "account"

        MDListItemHeadlineText:
            text: root.text
            
<CellEditSchedule@MDBoxLayout>:
    size_hint: None, None
    width: "220dp"
    height: "48dp"
    halign: 'center'
    valign: 'middle'

    canvas.before:
        Color:
            rgba: 0, 0, 0, 0.1
        Rectangle:
            pos: self.x - 2, self.y - 2
            size: self.width + 4, self.height + 4

    MDListItem:
        id: root.id
        on_release: app.selectSchedule(root.id)
        MDListItemLeadingIcon:
            icon: "account"

        MDListItemHeadlineText:
            text: root.text
            
<CellStudent@MDBoxLayout>:
    size_hint: None, None
    width: "220dp"
    height: "48dp"
    halign: 'center'
    valign: 'middle'

    canvas.before:
        Color:
            rgba: 0, 0, 0, 0.1
        Rectangle:
            pos: self.x - 2, self.y - 2
            size: self.width + 4, self.height + 4

    MDListItem:
        id: root.id
        on_release: app.showStudentCard(root.id)
        MDListItemLeadingIcon:
            icon: "account"

        MDListItemHeadlineText:
            text: root.text

<CellHead@MDBoxLayout>:
    size_hint: None, None
    width: "120dp"
    height: "48dp"
    halign: 'center'
    valign: 'middle'

    canvas.before:
        Color:
            rgba: [0.0, 0.5, 0.0, 0.3]
        RoundedRectangle:
            pos: self.pos
            size: self.size

    MDLabel:
        halign: 'center'
        valign: 'middle'
        bold: True
        text: root.text

<CellDefaultButton>:
    size_hint: None, None
    width: "120dp"
    height: "48dp"
    pos_hint: {"center_x": 0.5, "center_y": 0.5}
    orientation: 'vertical'
    padding: 10

    canvas.before:
        Color:
            rgba: 0, 0, 0, 0.1
        RoundedRectangle:
            pos: self.x - 2, self.y - 2
            size: self.width + 4, self.height + 4
            radius: [22,]

        Color:
            rgba: root.bgColor
        RoundedRectangle:
            pos: self.pos
            size: self.size
            radius: [20,]

    MDLabel:
        id: root.id
        text: root.text
        bold: True
        halign: 'center'
        valign: 'middle'

<CustomTable@MDBoxLayout>:
    orientation: 'horizontal'

    MDBoxLayout:
        size_hint_x: None
        width: "240dp"
        
        MDScrollView:
            id: scrollLView
            do_scroll_x: False
            on_scroll_y: app.sync_scroll("left", self.scroll_y)
        
            MDGridLayout:
                id: studentData
                cols: 1
                rows: app.rowsCount
                size_hint_y: None
                height: self.minimum_height
                default_size: None, dp(48)
                default_size_hint: 1, None
                spacing: "15dp"
                padding: [5,]
    
    MDBoxLayout:
        size_hint_x: 1
        padding: [10, 0, 20, 0]
        
        MDScrollView:
            id: scrollRView
            do_scroll_x: True
            on_scroll_y: app.sync_scroll("right", self.scroll_y)
            
            MDGridLayout:
                id: tableData
                cols: app.columnsCount
                rows: app.rowsCount
                size_hint_x: None
                size_hint_y: None
                width: self.minimum_width
                height: self.minimum_height
                default_size: dp(100), dp(48)
                default_size_hint: None, None
                spacing: "15dp"
                padding: [5,]
                
<SplashScreen@MDScreen>:
    name: 'splashScreen'

    MDFloatLayout:
        orientation: 'vertical'
        md_bg_color: [1, 1, 1, 1]
        size_hint: 1, 1
        
        MDLabel:
            text: ""
            font_style: "Title"
            role: "large"
            halign: "center"
            size_hint_y: None
            height: self.texture_size[1]
            bold: True
            pos_hint: {"center_x": 0.5, "center_y": 0.95}
            
        MDLabel:
            text: ""
            halign: "center"
            size_hint_y: None
            height: self.texture_size[1]
            pos_hint: {"center_x": 0.5, "center_y": .85}
        
        MDLabel:
            text: ""
            halign: "center"
            size_hint_y: None
            height: self.texture_size[1]
            pos_hint: {"center_x": 0.5, "center_y": 0.8}

        MDLabel:
            text: "Курсовой проект"
            font_style: "Title"
            halign: "center"
            size_hint_y: None
            height: self.texture_size[1]
            bold: True
            pos_hint: {"center_x": 0.5, "center_y": 0.65}
            
        MDLabel:
            text: ""
            halign: "center"
            size_hint_y: None
            height: self.texture_size[1]
            pos_hint: {"center_x": 0.5, "center_y": 0.6}

        MDLabel:
            text: "Приложение «Учет успеваемости и посещаемости лабораторных занятий»"
            halign: "center"
            size_hint_y: None
            height: self.texture_size[1]
            pos_hint: {"center_x": 0.5, "center_y": 0.55}

        FitImage:
            source: "pictures/ico.png"
            size_hint: None, None
            size: "180dp", "180dp"
            pos_hint: {"center_x": 0.25, 'center_y': 0.36}

        MDLabel:
            text: "Выполнил: "
            halign: "center"
            size_hint_y: None
            height: self.texture_size[1]
            pos_hint: {"center_x": 0.774, "center_y": 0.45}

        MDLabel:
            text: ""
            halign: "center"
            size_hint_y: None
            height: self.texture_size[1]
            pos_hint: {"center_x": 0.75, "center_y": 0.4}

        MDLabel:
            text: "Преподаватель: "
            halign: "center"
            size_hint_y: None
            height: self.texture_size[1]
            pos_hint: {"center_x": 0.753, "center_y": 0.35}

        MDLabel:
            text: ""
            halign: "center"
            size_hint_y: None
            height: self.texture_size[1]
            pos_hint: {"center_x": 0.763, "center_y": 0.3}

        MDLabel:
            text: ""
            halign: "center"
            size_hint_y: None
            height: self.texture_size[1]
            pos_hint: {"center_x": 0.5, "center_y": 0.1}
        
        MyIconButton:
            id: btnNext
            icon: "check-bold"
            width: "150dp"
            text: "Ок"
            pos_hint: {"center_x": 0.3,"center_y": 0.05}
            
            on_release: 
                app.changeScreen("mainScreen", "left")
                app.timer.forceStop()
                
        MyIconButton:
            icon: "window-close"
            width: "150dp"
            text: "Закрыть"
            pos_hint: {"center_x": 0.7,"center_y": 0.05}
            
            on_release: 
                app.close()


<MainScreen@MDScreen>:
    name: 'mainScreen'

    MDBoxLayout:
        orientation: 'horizontal'

        ################# Первый контейнер с NavRail###########
        MDBoxLayout:
            size_hint_x: None
            width: "80dp"
            NavRail:
                id: navRail
        ############### Второй контейнер, который займёт всё оставшееся пространство############
        MDBoxLayout:
            orientation: 'vertical'
            size_hint_x: 1
            size_hint_y: 1

            MDScreenManager:
                id: scrNestedManager
                
                ############### HomeScreen ###########
                MDScreen:
                    name: "home"
                    MDBoxLayout:
                        md_bg_color: app.theme_cls.surfaceColor
                        orientation: 'vertical'
                        size_hint: 1, 1
                
                        MDScrollView:
                            do_scroll_x: False
                            do_scroll_y: True
                
                            MDBoxLayout:
                                orientation: 'horizontal'
                                md_bg_color: app.theme_cls.surfaceColor
                                size_hint_y: None
                                height: self.minimum_height
                                padding: 20
                                spacing: 10
                                pos_hint: {"top": 1}
                
                                HomeWidgetInfo:
                                    id: "homeLN"
                                    text: "Latest News"
                                    size_hint_x: 0.8
                                    size_hint_y: None
                                    height: "600dp" 
                
                                MDBoxLayout:
                                    orientation: 'vertical'
                                    size_hint_x: 0.2
                                    spacing: 10
                                    pos_hint: {"top": 1}
                
                                    HomeWidgetInfo:
                                        id: "homeCh"
                                        text: "Changes"
                                        size_hint_x: 1
                                        size_hint_y: None
                                        height: "300dp"
                                        pos_hint: {"top": 1}
                
                                    HomeWidgetInfo:
                                        id: "homeEv"
                                        text: "Events"
                                        size_hint_x: 1
                                        size_hint_y: None
                                        height: "180dp"
                                        pos_hint: {"top": 1}
                
                ################SelectSubjectScreen############
                MDScreen:
                    name: "selectSubjectScreen"
                
                    MDBoxLayout:
                        orientation: 'vertical'
                        md_bg_color: app.theme_cls.surfaceColor
                        padding: 20
                        spacing: 10
                        size_hint: 1, 1
                
                        ScrollView:
                            id: scrollSubject
                            do_scroll_y: False
                            do_scroll_x: True
                            
                ################SelectSubjectSelectScreen############
                MDScreen:
                    name: "selectSubjectSelectScreen"
                
                    MDBoxLayout:
                        orientation: 'vertical'
                        md_bg_color: app.theme_cls.surfaceColor
                        padding: 20
                        spacing: 10
                        size_hint: 1, 1
                
                        ScrollView:
                            id: scrollSubjectSelect
                            do_scroll_y: False
                            do_scroll_x: True
                                        
                ################viewGroupScreen############
                MDScreen:
                    name: "viewGroupScreen"
                
                    MDBoxLayout:
                        orientation: 'vertical'
                        md_bg_color: app.theme_cls.surfaceColor
                        padding: 20
                        spacing: 10
                        size_hint: 1, 1
                
                        ScrollView:
                            id: scrollGroupNested
                            do_scroll_y: False
                            do_scroll_x: True
                            
                ################ManageGroupScreen############
                MDScreen:
                    name: "manageGroupScreen"
                    MDBoxLayout:
                        orientation: 'vertical'
                        md_bg_color: app.theme_cls.surfaceColor
                        padding: 20
                        spacing: 10
                        size_hint: 1, 1
                
                        ScrollView:
                            id: scrollMe
                            do_scroll_y: False
                            do_scroll_x: True
                        
                            NavGroup:
                                id: navGroupManage
                                cols: 5
                                    
                                ChangeGroupItem:
                                    image: "pictures/edit.jpg"
                                    text: "Students Data"
                                    on_release: 
                                        app.changeNestedScreen("editStudentScreen", "left")
                                        app.createStudentEditList()
                                        app.selectedStudent = None
                                    
                                ChangeGroupItem:
                                    image: "pictures/addShedule.jpg"
                                    text: "Schedule"
                                    on_release: 
                                        app.changeNestedScreen("selectSubjectSelectScreen", "left")
                                    
                                ChangeGroupItem:
                                    image: "pictures/delete.jpg"
                                    text: "Remove Group"
                                    on_release:
                                        app.deleteGroup()
                                        app.changeNestedScreen("changeGroup", "left")
                                
                                ChangeGroupItem:
                                    image: "pictures/return.jpg"
                                    text: "Return"
                                    on_release: app.changeNestedScreen("changeGroup", "left")
                            
                        
                        
                ################AddNewGroupScreen############
                MDScreen:
                    name: "addNewGroupScreen"
                    
                    MDBoxLayout:
                        md_bg_color: app.theme_cls.surfaceColor
                        orientation: 'vertical'
                        padding: 5
                        spacing: 5
                        size_hint: 1, None
                        height: "50dp"
                        pos_hint: {"top": 1}
                        
                        MyButton:
                            text: "Return"
                            pos_hint: {"left": 1, "top": 1}
                            on_release: app.changeNestedScreen("changeGroup", "left")
                            
                    MDBoxLayout:
                        md_bg_color: app.theme_cls.surfaceColor
                        orientation: 'vertical'
                        padding: 5
                        spacing: 10
                        size_hint: 1, None
                        height: root.height - 50
                        
                        MDFloatLayout:
                            orientation: 'vertical'
                            size_hint: None, 1
                            width: "500dp"
                            spacing: 10
                            pos_hint: {"center_x": 0.5}
                            
                            canvas.before:
                                Color:
                                    rgba: 0, 0, 0, 0.1
                                RoundedRectangle:
                                    pos: self.x - 2, self.y - 2
                                    size: self.width + 4, self.height + 4
                                    radius: [18,]
                                Color:
                                    rgba: 1, 1, 1, 1
                                RoundedRectangle:
                                    pos: self.x, self.y
                                    size: self.width, self.height
                                    radius: [18,]
                                    
                            FitImage:
                                source: "pictures/ico.png"
                                size_hint: None, None
                                size: "150dp", "150dp"
                                pos_hint: {"center_x": 0.5, "top": 0.95}
                                radius: [50,]
                                    
                            MDTextField:
                                id: groupTextField
                                mode: "outlined"
                                theme_line_color: "Custom"
                                line_color_focus: "green"
                                size_hint: None, None
                                width: "400dp"
                                pos_hint: {"center_x": 0.5, "top": 0.6}
                                bold: True
                                
                                MDTextFieldLeadingIcon:
                                    icon: "group-outlined"
                                    
                                MDTextFieldHintText:
                                    text: "Group Name"
                                    
                            MDButton:
                                style: "elevated"
                                pos_hint: {"center_x": .5, "top": .4}
                                size_hint: None, None
                                width: "300dp"
                                height: "50dp"
                                on_release: app.createGroup()
                        
                                MDButtonIcon:
                                    icon: "plus"
                        
                                MDButtonText:
                                    text: "Create"
                                    bold: True

                ################EditStudentData############
                MDScreen:
                    name: "editStudentScreen"
                    
                    MDBoxLayout:
                        orientation: 'vertical'
                        
                        MDBoxLayout:
                            md_bg_color: app.theme_cls.surfaceColor
                            size_hint_y: None
                            height: "50dp"
                            padding: 5
                            spacing: 5
                            
                            MyButton:
                                text: "Return"
                                pos_hint: {"left": 1, "center_y": 0.5}
                                on_release: app.changeNestedScreen("manageGroupScreen", "left")
                        
                        MDBoxLayout:
                            md_bg_color: app.theme_cls.surfaceColor
                            orientation: 'horizontal'
                            spacing: 10
                            padding: 10
                            
                            Widget:
                                size_hint: None, 1
                                width: "200dp"
                            
                            MDBoxLayout:
                                md_bg_color: app.theme_cls.surfaceColor
                                orientation: 'vertical'
                                size_hint: None, 1
                                width: "240dp"
                                spacing: 10
                                
                                MDScrollView:
                                    do_scroll_y: True
                                    do_scroll_x: False
                                    
                                    MDGridLayout:
                                        id: studentEditData
                                        cols: 1
                                        size_hint_y: None
                                        height: self.minimum_height
                                        default_size: None, dp(48)
                                        default_size_hint: 1, None
                                        padding: [5,]
                                        spacing: "15dp"
                                        
                            Widget:
                                size_hint: None, 1
                                width: "20dp"
                            
                            MDFloatLayout:
                                size_hint: None, 1
                                width: "500dp"
                                pos_hint: {"right": 1}
                                
                                canvas.before:
                                    Color:
                                        rgba: 0, 0, 0, 0.1
                                    RoundedRectangle:
                                        pos: self.x - 2, self.y - 2
                                        size: self.width + 4, self.height + 4
                                        radius: [18,]
                                    Color:
                                        rgba: 1, 1, 1, 1
                                    RoundedRectangle:
                                        pos: self.x, self.y
                                        size: self.width, self.height
                                        radius: [18,]
                                        
                                FitImage:
                                    source: "pictures/ico.png"
                                    size_hint: None, None
                                    size: "150dp", "150dp"
                                    pos_hint: {"center_x": 0.5, "top": 0.95}
                                    radius: [50,]
                                    
                                MDTextField:
                                    id: studentEditLastName
                                    mode: "outlined"
                                    theme_line_color: "Custom"
                                    line_color_focus: "green"
                                    size_hint: None, None
                                    width: "400dp"
                                    pos_hint: {"center_x": 0.5, "top": 0.65}
                                    bold: True
                                    
                                    MDTextFieldLeadingIcon:
                                        icon: "account"
                                        
                                    MDTextFieldHintText:
                                        text: "Student Last Name"
                                        
                                MDTextField:
                                    id: studentEditName
                                    mode: "outlined"
                                    theme_line_color: "Custom"
                                    line_color_focus: "green"
                                    size_hint: None, None
                                    width: "400dp"
                                    pos_hint: {"center_x": 0.5, "top": 0.55}
                                    bold: True
                                    
                                    MDTextFieldLeadingIcon:
                                        icon: "account"
                                        
                                    MDTextFieldHintText:
                                        text: "Student Name"
                                        
                                MDTextField:
                                    id: studentEditMiddleName
                                    mode: "outlined"
                                    theme_line_color: "Custom"
                                    line_color_focus: "green"
                                    size_hint: None, None
                                    width: "400dp"
                                    pos_hint: {"center_x": 0.5, "top": 0.45}
                                    bold: True
                                    
                                    MDTextFieldLeadingIcon:
                                        icon: "account"
                                        
                                    MDTextFieldHintText:
                                        text: "Student Middle Name"
                                        
                                MDTextField:
                                    id: studentEditPhone
                                    mode: "outlined"
                                    theme_line_color: "Custom"
                                    line_color_focus: "green"
                                    size_hint: None, None
                                    width: "400dp"
                                    pos_hint: {"center_x": 0.5, "top": 0.35}
                                    bold: True
                                    
                                    MDTextFieldLeadingIcon:
                                        icon: "phone"
                                        
                                    MDTextFieldHintText:
                                        text: "Student Phone Number"

                                MDTextField:
                                    id: studentEditEmail
                                    mode: "outlined"
                                    theme_line_color: "Custom"
                                    line_color_focus: "green"
                                    size_hint: None, None
                                    width: "400dp"
                                    pos_hint: {"center_x": 0.5, "top": 0.25}
                                    bold: True
                                    
                                    MDTextFieldLeadingIcon:
                                        icon: "mail"
                                        
                                    MDTextFieldHintText:
                                        text: "Student Email"
                                        
                                MyIconButton:
                                    icon: "plus"
                                    text: "Add"
                                    pos_hint: {"center_x": .2, "top": 0.1}
                                    on_release: app.addStudent()
                                        
                                MyIconButton:
                                    icon: "content-save"
                                    text: "Edit"
                                    pos_hint: {"center_x": .5, "top": 0.1}
                                    on_release: app.editStudent()
                                    
                                MyIconButton:
                                    icon: "delete-forever"
                                    text: "Delete"
                                    pos_hint: {"center_x": .8, "top": 0.1}
                                    on_release: app.deleteStudent()
                        
                ################Shedule for Group############
                MDScreen:
                    name: "editSheduleScreen"  
                    
                    MDBoxLayout:
                        orientation: 'vertical'
                        
                        MDBoxLayout:
                            md_bg_color: app.theme_cls.surfaceColor
                            size_hint_y: None
                            height: "50dp"
                            padding: 5
                            spacing: 5
                            
                            MyButton:
                                text: "Return"
                                pos_hint: {"left": 1, "center_y": 0.5}
                                on_release: app.changeNestedScreen("manageGroupScreen", "left")
                        
                        MDBoxLayout:
                            md_bg_color: app.theme_cls.surfaceColor
                            orientation: 'horizontal'
                            spacing: 10
                            padding: 10
                            
                            Widget:
                                size_hint: None, 1
                                width: "200dp"
                            
                            MDBoxLayout:
                                md_bg_color: app.theme_cls.surfaceColor
                                orientation: 'vertical'
                                size_hint: None, 1
                                width: "240dp"
                                spacing: 10
                                
                                MDScrollView:
                                    do_scroll_y: True
                                    do_scroll_x: False
                                    
                                    MDGridLayout:
                                        id: sheduleEditData
                                        cols: 1
                                        size_hint_y: None
                                        height: self.minimum_height
                                        default_size: None, dp(48)
                                        default_size_hint: 1, None
                                        padding: [5,]
                                        spacing: "15dp"
                                        
                            Widget:
                                size_hint: None, 1
                                width: "20dp"
                            
                            MDFloatLayout:
                                size_hint: None, 1
                                width: "500dp"
                                pos_hint: {"right": 1}
                                
                                canvas.before:
                                    Color:
                                        rgba: 0, 0, 0, 0.1
                                    RoundedRectangle:
                                        pos: self.x - 2, self.y - 2
                                        size: self.width + 4, self.height + 4
                                        radius: [18,]
                                    Color:
                                        rgba: 1, 1, 1, 1
                                    RoundedRectangle:
                                        pos: self.x, self.y
                                        size: self.width, self.height
                                        radius: [18,]
                                        
                                FitImage:
                                    source: "pictures/ico.png"
                                    size_hint: None, None
                                    size: "150dp", "150dp"
                                    pos_hint: {"center_x": 0.5, "top": 0.95}
                                    radius: [50,]
                                    
                                MDTextField:
                                    id: txtFieldD
                                    readonly: True
                                    pos_hint: {"center_x": .3, "top": .6}
                                    size_hint: None, None
                                    width: "100dp"
                                    height: "50dp"
                                    bold: True
                                    halign: 'center'
                                    
                                    MDTextFieldHintText:
                                        text: "Day"
                        
                                MDTextField:
                                    id: txtFieldM
                                    readonly: True
                                    hint_text: "Month"
                                    pos_hint: {"center_x": .5, "top": .6}
                                    size_hint: None, None
                                    width: "100dp"
                                    height: "50dp"
                                    bold: True
                                    halign: 'center'
                                    
                                    MDTextFieldHintText:
                                        text: "Month"
                        
                                MDTextField:
                                    id: txtFieldY
                                    readonly: True
                                    hint_text: "Year"
                                    pos_hint: {"center_x": .7, "top": .6}
                                    size_hint: None, None
                                    width: "100dp"
                                    height: "50dp"
                                    bold: True
                                    halign: 'center'
                                    
                                    MDTextFieldHintText:
                                        text: "Year"
                                                                
                                MyIconButton:
                                    id: buttonD
                                    icon: "plus-box"
                                    text: "Set Day"
                                    width: "140dp"
                                    pos_hint: {"center_x": .2, "top": 0.3}
                                    on_release: app.menuD.open()
                                        
                                MyIconButton:
                                    id: buttonM
                                    icon: "plus-box"
                                    text: "Set Month"
                                    width: "140dp"
                                    pos_hint: {"center_x": .5, "top": 0.3}
                                    on_release: app.menuM.open()
                                    
                                MyIconButton:
                                    id: buttonY
                                    icon: "plus-box"
                                    text: "Set Year"
                                    width: "140dp"
                                    pos_hint: {"center_x": .8, "top": 0.3}
                                    on_release: app.menuY.open()
                                    
                                MyIconButton:
                                    icon: "plus"
                                    text: "Append"
                                    width: "140dp"
                                    pos_hint: {"center_x": .3, "top": 0.15}
                                    on_release: app.appendShedule()
                                    
                                MyIconButton:
                                    icon: "trash-can"
                                    text: "Delete"
                                    width: "140dp"
                                    pos_hint: {"center_x": .7, "top": 0.15}
                                    on_release: app.removeShedule()
                                    
                 ################### ViewScreen ####################   
                MDScreen:
                    name: "viewStudents"

                    ###########Instruments###########

                    MDBoxLayout:
                        md_bg_color: app.theme_cls.surfaceColor
                        orientation: 'horizontal'
                        size_hint: 1, 0.1
                        pos_hint: {'top': 1}
                        spacing: 30
                        
                        MyButton:
                            text: "Return"
                            pos_hint: {"left": 1, "top": 0.8}
                            padding: 10
                            on_release: app.changeNestedScreen("selectSubjectScreen", "left")
                        
                        InstrumentPlace:
                            id: instrumentPlace
                            pos_hint: {'left': 0.7, 'center_y': 0.5}
                            
                        MyIconButton:
                            id: buttonTableMonth
                            icon: "calendar-month"
                            text: f"Set Date [ShowAll]"
                            width: "200dp"
                            pos_hint: {"right": 1, "top": 0.8}
                            padding: 10
                            on_release: app.menuT.open()
                            
                        MyIconButton:
                            icon: "content-save-all"
                            width: "160dp"
                            text: "Save Grades"
                            pos_hint: {"right": 1, "top": 0.8}
                            padding: 10
                            on_release: app.updateStudentsData()



                    ###############BoxWithTableAndStudentInfo###############
                    MDBoxLayout:
                        id: tableFloatLayout
                        md_bg_color: app.theme_cls.surfaceColor
                        orientation: 'horizontal'
                        size_hint: 1, 0.9
                        padding: 10
                        spacing: 10

                        CustomTable:
                            id: custom_table
                            size_hint: None,None
                            width: root.width - navRail.width
                            height: root.height - 100
                            pos_hint: {'top': 1}

                ############### ChangeGroupScreen ###########
                MDScreen:
                    name: "changeGroup"
                
                    MDBoxLayout:
                        orientation: 'vertical'
                        md_bg_color: app.theme_cls.surfaceColor
                        padding: 20
                        spacing: 10
                        size_hint: 1, 1
                
                        ScrollView:
                            id: scrollGroup
                            do_scroll_y: False
                            do_scroll_x: True
                            
                ############### SettingsScreen ###########
                MDScreen:
                    name: "settings"
                    MDFloatLayout:
                        id: settingsFloat
                        md_bg_color: app.theme_cls.surfaceColor
                        orientation: 'vertical'
                        
                        SettingsWidgetInfo:
                            width: "400dp"
                            height: "150dp"
                            pos_hint: {"center_x": 0.2, "center_y": 0.7}
                        
                        ColorSettingsWidgetInfo:
                            width: "200dp"
                            height: "300dp"
                            pos_hint: {"center_x": 0.5, "center_y": 0.7}
                        
                        ModeSettingsWidgetInfo:
                            width: "200dp"
                            height: "300dp"
                            pos_hint: {"center_x": 0.7, "center_y": 0.7}
                        

                ############### HelpScreen ###########
                MDScreen:
                    name: "help"
                    MDFloatLayout:
                        md_bg_color: app.theme_cls.surfaceColor
                        orientation: 'vertical'
                        
                        HelpWidgetPrg:
                            width: "500dp"
                            height: "600dp"
                            pos_hint: {"center_x": 0.25, "center_y": 0.5}
                            
                        HelpWidgetAuthor:
                            width: "500dp"
                            height: "600dp"
                            pos_hint: {"center_x": 0.75, "center_y": 0.5}
                        
                        
                        


"""


class Timer:
    def __init__(self):
        self.time = 0

    def start(self):
        self.update()

    def update(self, dt=0):
        if self.time < 60:

            try:
                widget = MDApp.get_running_app().root.get_screen("splashScreen")
                widget.ids.btnNext.text = f"Ок [{60 - self.time}]"

            except AttributeError:
                pass

            self.time += 1
            self.event = Clock.schedule_once(self.update, 1)
        else:
            app = MDApp.get_running_app()
            app.close()

    def forceStop(self):
        self.event.cancel()


class MenuHeader(MDBoxLayout):
    pass


class ChangeGroupItem(ButtonBehavior, MDBoxLayout):
    image = StringProperty()
    text = StringProperty()


class HomeWidgetInfo(MDBoxLayout):
    text = StringProperty()
    infoOfWidget = StringProperty("Your Information will be here")


class SettingsWidgetInfo(MDBoxLayout):
    pass


class CellDefaultButton(ButtonBehavior, MDBoxLayout, HoverBehavior):
    bgColor = ObjectProperty([1, 1, 1, 1])
    text = StringProperty()

    def on_enter(self):
        self.bgColor = [0.9, 0.9, 0.9, 1]

    def on_leave(self):
        self.bgColor = [1, 1, 1, 1]

    def on_press(self):
        self.bgColor = [0.8, 0.8, 0.8, 1]

    def on_release(self):
        self.bgColor = [1, 1, 1, 1]
        MDApp.get_running_app().printID(self.id)


class InstrumentButton(ButtonBehavior, HoverBehavior, MDFloatLayout):
    icon = StringProperty()
    value = StringProperty()
    mainIcon = StringProperty()
    posIcon = ObjectProperty({'center_x': 0.3, 'center_y': 0.5})
    posMainIcon = ObjectProperty({'center_x': 0.5, 'center_y': 0.5})

    def on_enter(self):
        Animation(md_bg_color=[0, 0.4, 0, 0.6], d=0.2).start(self)

    def on_leave(self):
        Animation(md_bg_color=[0, 0.4, 0, 0.3], d=0.2).start(self)

    def on_press(self):
        for button in self.parent.children:
            if button.icon == "check":
                button.icon = ""
                button.posMainIcon = {'center_x': 0.5, 'center_y': 0.5}

        self.icon = "check"
        self.posMainIcon = {'center_x': 0.7, 'center_y': 0.5}

    def on_release(self):
        MDApp.get_running_app().currentMark = self.value


class MyButton(ButtonBehavior, MDBoxLayout, HoverBehavior):
    icon = StringProperty("arrow-left")
    text = StringProperty()
    fontSize = NumericProperty("16sp")
    fontName = StringProperty("Roboto")
    bgColor = ObjectProperty([0.0, 0.5, 0.0, 0.3])

    def on_enter(self):
        Animation(bgColor=[0.0, 0.5, 0.0, 0.6], d=0.2).start(self)

    def on_leave(self):
        Animation(bgColor=[0.0, 0.5, 0.0, 0.3], d=0.2).start(self)

    def on_press(self):
        self.bgColor = [0.0, 0.5, 0.0, 0.6]

    def on_release(self):
        Animation(bgColor=[0.0, 0.5, 0.0, 0.3], d=0.2).start(self)


class MyIconButton(ButtonBehavior, MDBoxLayout, HoverBehavior):
    icon = StringProperty()
    text = StringProperty()
    fontSize = NumericProperty("16sp")
    fontName = StringProperty("Roboto")
    bgColor = ObjectProperty([0.0, 0.5, 0.0, 0.3])

    def on_enter(self):
        Animation(bgColor=[0.0, 0.5, 0.0, 0.6], d=0.2).start(self)

    def on_leave(self):
        Animation(bgColor=[0.0, 0.5, 0.0, 0.3], d=0.2).start(self)

    def on_press(self):
        self.bgColor = [0.0, 0.5, 0.0, 0.6]

    def on_release(self):
        Animation(bgColor=[0.0, 0.5, 0.0, 0.3], d=0.2).start(self)


class StudentInfoWidget(MDListItem):
    icon = StringProperty()
    text = StringProperty()


class StudentInfoLayout(MDBoxLayout):
    pass


class CellStudentHead(MDBoxLayout):
    text = StringProperty()


class MyTooltip(MDTooltip):
    txtTooltipHead = StringProperty()
    txtTooltipBody = StringProperty()


class NavItem(MyTooltip, MDIconButton):
    txtTooltip = StringProperty()


class MDFabCustomButton(MyTooltip, MDFabButton):
    txtTooltipHead = StringProperty()
    txtTooltipBody = StringProperty()


class CellHead(MDBoxLayout):
    text = StringProperty()


class CellStudent(MDBoxLayout):
    text = StringProperty()


class CellEditStudent(MDBoxLayout):
    text = StringProperty()


class CellEditSchedule(MDBoxLayout):
    text = StringProperty()


class NavGroup(MDGridLayout):
    id = StringProperty()
    cols = NumericProperty()


class Journal(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.menuD = None
        self.menuM = None
        self.menuY = None
        self.timer = Timer()

        self.menuDays = [
            {
                "text": f"Day: {i}",
                "on_release": lambda x=f"{i}": self.setText("txtFieldD", x),
            } for i in range(1, 32)
        ]
        self.menuMonth = [
            {
                "text": f"Month: {i}",
                "on_release": lambda x=f"{i}": self.setText("txtFieldM", x),
            } for i in range(1, 13)
        ]
        self.menuYears = [
            {
                "text": f"Year: {i}",
                "on_release": lambda x=f"{i}": self.setText("txtFieldY", x),
            } for i in range(2023, 2030)
        ]

        self.menuTable = [
                             {
                                 "text": "ShowAll",
                                 "on_release": lambda x="showAll": self.setTableMonth(x),
                             }
                         ] + [
                             {
                                 "text": f"Month: {i}",
                                 "on_release": lambda x=f"{i}": self.setTableMonth(x),
                             } for i in range(1, 13)
                         ]

        self.dates = []
        self.data = []
        self.students = []
        self.groups = []
        self.subjects = None
        self.countOfGroups = 1
        self.countOfStudents = None
        self.rowsCount = None
        self.columnsCount = None
        self.selectedGroupID = None
        self.currentMonth = "06"
        self.selectedStudentID = None
        self.showAll = True

        self.currentMark = "view"
        self.selectedShedule = None
        self.selectedSubjectID = None

    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Green"

        Window.size = (1250, 750)
        Window.minimum_width, Window.minimum_height = 1250, 750
        Window.multisamples = 2

        self.title = "Modern journal"
        self.icon = "pictures/ico.png"


        self.timer.start()

        return Builder.load_string(KV)

    def changeTheme(self, colorName):
        if colorName == "Red":
            self.theme_cls.primary_palette = "Red"
        elif colorName == "Green":
            self.theme_cls.primary_palette = "Green"
        elif colorName == "Blue":
            self.theme_cls.primary_palette = "Blue"

    def changeThemeMode(self, mode):
        if mode == "Light":
            self.theme_cls.theme_style = "Light"
        elif mode == "Dark":
            self.theme_cls.theme_style = "Dark"

    def appendShedule(self):
        try:
            day = self.root.get_screen('mainScreen').ids.txtFieldD.text
            month = self.root.get_screen('mainScreen').ids.txtFieldM.text
            year = self.root.get_screen('mainScreen').ids.txtFieldY.text

            if len(day) == 1:
                day = f"0{day}"

            if len(month) == 1:
                month = f"0{month}"

            date = f"{year}-{month}-{day}"

            db = Database()
            db.addShedule(self.selectedGroupID, self.selectedSubjectID, date)
            db.close()

            self.root.get_screen('mainScreen').ids.txtFieldD.text = ""
            self.root.get_screen('mainScreen').ids.txtFieldM.text = ""
            self.root.get_screen('mainScreen').ids.txtFieldY.text = ""

            self.resetWidgetSchedule()

            self.snackBarAppend(True)
        except:
            self.snackBarAppend(False)

    def close(self):
        self.stop()

    def setTableMonth(self, key):
        if key == "showAll":
            self.showAll = True
            self.root.get_screen('mainScreen').ids.buttonTableMonth.text = f"Set Date [showAll]"
        else:
            self.showAll = False
            if len(key) == 1:
                key = f"0{key}"
                self.root.get_screen('mainScreen').ids.buttonTableMonth.text = f"Set Date [{key}]"
                self.currentMonth = key
            else:
                self.root.get_screen('mainScreen').ids.buttonTableMonth.text = f"Set Date [{key}]"
                self.currentMonth = key

        self.createTable(self.selectedGroupID, self.selectedSubjectID, self.currentMonth, self.showAll)

    def setText(self, fieldID, value):
        self.root.get_screen('mainScreen').ids[fieldID].text = value

    def homeClick(self, intance):
        rail = self.root.get_screen('mainScreen').ids.navRail

        for item in rail.children:
            item.style = "standard"

        self.changeNestedScreen("home", "left")

    def railClick(self, intance, screen):
        rail = self.root.get_screen('mainScreen').ids.navRail

        for item in rail.children:
            item.style = "standard"

        intance.style = "tonal"
        self.changeNestedScreen(screen, "left")

    def changeNestedScreen(self, screenName, direction):
        self.root.get_screen('mainScreen').ids.scrNestedManager.current = screenName
        self.root.get_screen('mainScreen').ids.scrNestedManager.transition.direction = direction

    def changeScreen(self, screenName, direction):
        self.root.transition = MDSlideTransition(direction=direction)
        self.root.current = screenName

    def sync_scroll(self, source, scroll_y_value):
        if source == "left":
            self.root.get_screen('mainScreen').ids.custom_table.ids.scrollRView.scroll_y = scroll_y_value
        elif source == "right":
            self.root.get_screen('mainScreen').ids.custom_table.ids.scrollLView.scroll_y = scroll_y_value

    def setCurrentGroupID(self, groupID):
        self.selectedGroupID = groupID

    def createStudentEditList(self):
        studentData = self.root.get_screen('mainScreen').ids.studentEditData

        db = Database()
        self.students = db.getStudentsToEdit(self.selectedGroupID)
        db.close()

        for child in list(studentData.children):
            studentData.remove_widget(child)

        for student in self.students:
            studentData.add_widget(CellEditStudent(text=student[1] + " " + student[2][0] + "." + student[3][0] + ".",
                                                   id=str(student[0])))

    def showStudentEdit(self, studentID):

        self.selectedStudentID = studentID
        studentName = self.root.get_screen('mainScreen').ids.studentEditName
        studentLastName = self.root.get_screen('mainScreen').ids.studentEditLastName
        studentMiddleName = self.root.get_screen('mainScreen').ids.studentEditMiddleName
        studentPhone = self.root.get_screen('mainScreen').ids.studentEditPhone
        studentEmail = self.root.get_screen('mainScreen').ids.studentEditEmail

        studentName.text = ""
        studentLastName.text = ""
        studentMiddleName.text = ""
        studentPhone.text = ""
        studentEmail.text = ""

        for student in self.students:
            if student[0] == int(studentID):
                studentLastName.text = student[1]
                studentName.text = student[2]
                studentMiddleName.text = student[3]
                studentPhone.text = str(student[4])
                studentEmail.text = str(student[5])

    def updateStudentsData(self):
        try:
            db = Database()
            db.updateStudents(self.students, self.selectedSubjectID)
            db.close()
            self.snackBarUpdateStudents(True)
        except:
            self.snackBarUpdateStudents(False)

    def showShedule(self):
        self.selectedSheduleID = None
        day = self.root.get_screen('mainScreen').ids.txtFieldD
        month = self.root.get_screen('mainScreen').ids.txtFieldM
        year = self.root.get_screen('mainScreen').ids.txtFieldY

        day.text = ""
        month.text = ""
        year.text = ""

        db = Database()
        self.shedules = db.getShedulesToEdit(self.selectedGroupID, self.selectedSubjectID)
        db.close()

        sheduleID = self.root.get_screen('mainScreen').ids.sheduleEditData

        for child in list(sheduleID.children):
            sheduleID.remove_widget(child)

        for date in self.shedules:
            newDate = date[0].split("-")
            newDate = newDate[2] + '.' + newDate[1] + '.' + newDate[0]
            sheduleID.add_widget(CellEditSchedule(text=str(newDate), id=str(date[1])))

    def selectSchedule(self, sheduleID):
        self.selectedSheduleID = sheduleID

        txtDay = self.root.get_screen('mainScreen').ids.txtFieldD
        txtMonth = self.root.get_screen('mainScreen').ids.txtFieldM
        txtYear = self.root.get_screen('mainScreen').ids.txtFieldY

        for date in self.shedules:
            if date[1] == int(sheduleID):
                day = date[0].split("-")[2]
                month = date[0].split("-")[1]
                year = date[0].split("-")[0]

                txtDay.text = day
                txtMonth.text = month
                txtYear.text = year

    def removeShedule(self):
        try:
            db = Database()
            db.removeShedule(self.selectedSheduleID)
            db.close()

            self.resetWidgetSchedule()

            self.snackBarRemoveShedule(True)
        except:
            self.snackBarRemoveShedule(False)

    def deleteStudent(self):
        try:
            db = Database()
            db.removeStudent(self.selectedStudentID)
            db.close()

            self.resetWidgetStudents()

            self.snackBarRemoveStudent(True)
        except:
            self.snackBarRemoveStudent(False)

    def editStudent(self):
        try:
            studentObj = Student(id=self.selectedStudentID,
                                 lastName=self.root.get_screen('mainScreen').ids.studentEditLastName.text,
                                 firstName=self.root.get_screen('mainScreen').ids.studentEditName.text,
                                 middleName=self.root.get_screen('mainScreen').ids.studentEditMiddleName.text,
                                 phone=self.root.get_screen('mainScreen').ids.studentEditPhone.text,
                                 email=self.root.get_screen('mainScreen').ids.studentEditEmail.text,
                                 grades=[])

            db = Database()
            db.editStudentAsObject(studentObj, self.selectedGroupID)
            db.close()

            self.resetWidgetStudents()

            self.snackBarEditStudent(True)
        except:
            self.snackBarEditStudent(False)

    def addStudent(self):
        try:
            studentObj = Student(id=None,
                                 lastName=self.root.get_screen('mainScreen').ids.studentEditLastName.text,
                                 firstName=self.root.get_screen('mainScreen').ids.studentEditName.text,
                                 middleName=self.root.get_screen('mainScreen').ids.studentEditMiddleName.text,
                                 phone=self.root.get_screen('mainScreen').ids.studentEditPhone.text,
                                 email=self.root.get_screen('mainScreen').ids.studentEditEmail.text,
                                 grades=[])

            db = Database()
            db.addStudentAsObject(studentObj, self.selectedGroupID)
            db.close()

            self.resetWidgetStudents()

            self.snackBarAddStudent(True)
        except:
            self.snackBarAddStudent(False)

    def resetWidgetStudents(self):
        studentData = self.root.get_screen('mainScreen').ids.studentEditData

        db = Database()
        self.students = db.getStudentsToEdit(self.selectedGroupID)
        db.close()

        for child in list(studentData.children):
            studentData.remove_widget(child)

        for student in self.students:
            studentData.add_widget(CellEditStudent(text=student[1] + " " + student[2][0] + "." + student[3][0] + ".",
                                                   id=str(student[0])))

    def resetWidgetSchedule(self):
        sheduleData = self.root.get_screen('mainScreen').ids.sheduleEditData

        db = Database()
        self.shedules = db.getShedulesToEdit(self.selectedGroupID, self.selectedSubjectID)
        db.close()

        for child in list(sheduleData.children):
            sheduleData.remove_widget(child)

        for date in self.shedules:
            newDate = date[0].split("-")
            newDate = newDate[2] + '.' + newDate[1] + '.' + newDate[0]
            sheduleData.add_widget(CellEditSchedule(text=str(newDate), id=str(date[1])))

    def createGroup(self):
        groupField = self.root.get_screen('mainScreen').ids.groupTextField.text

        try:
            db = Database()
            db.addGroup(groupField)
            db.close()
            self.resetWidgets()
            self.snackBarCrGroup(groupField, True)
        except:
            self.snackBarCrGroup(groupField, False)

        self.root.get_screen('mainScreen').ids.groupTextField.text = ""

    def setSelectedSubjectID(self, subjectID):
        self.selectedSubjectID = subjectID

    def on_start(self):
        test = Database()
        self.groups = test.getGroups()
        self.subjects = test.getSubjects()
        self.subjectsBg = {
            "1": "pictures/python.jpg",
            "2": "pictures/math.jpg",
            "3": "pictures/csharp.jpg",
            "4": "pictures/cplus.jpg"
        }
        test.close()

        self.menuD = MDDropdownMenu(
            header_cls=MenuHeader(),
            caller=self.root.get_screen('mainScreen').ids.buttonD,
            items=self.menuDays,
            width_mult=4,
        )

        self.menuM = MDDropdownMenu(
            header_cls=MenuHeader(),
            caller=self.root.get_screen('mainScreen').ids.buttonM,
            items=self.menuMonth,
            width_mult=4,
        )

        self.menuY = MDDropdownMenu(
            header_cls=MenuHeader(),
            caller=self.root.get_screen('mainScreen').ids.buttonY,
            items=self.menuYears,
            width_mult=4,
        )

        self.menuT = MDDropdownMenu(
            header_cls=MenuHeader(),
            caller=self.root.get_screen('mainScreen').ids.buttonTableMonth,
            items=self.menuTable,
            width_mult=4,
        )

        for group in self.groups:
            self.countOfGroups += 1

        self.root.get_screen('mainScreen').ids.scrollGroup.add_widget(NavGroup(id="areaGroup",
                                                                               cols=self.countOfGroups))
        self.root.get_screen('mainScreen').ids.scrollGroupNested.add_widget(NavGroup(id="areaGroupNested",
                                                                                     cols=self.countOfGroups))
        self.root.get_screen('mainScreen').ids.scrollSubject.add_widget(NavGroup(id="areaSubject",
                                                                                 cols=len(self.subjects) + 1))

        self.root.get_screen('mainScreen').ids.scrollSubjectSelect.add_widget(NavGroup(id="areaSubjectSelect",
                                                                                 cols=len(self.subjects) + 1))

        for subject in self.subjects:
            self.root.get_screen('mainScreen').ids.scrollSubject.children[0].add_widget(
                ChangeGroupItem(
                    id=f"Sub{subject[0]}",
                    image=self.subjectsBg.get(str(subject[0]), "pictures/default.jpg"),
                    text=subject[1],
                    on_release=lambda x, sub = subject[0]: (self.setSelectedSubjectID(sub),
                    self.changeNestedScreen("viewStudents", "left"),
                    self.createTable(self.selectedGroupID, self.selectedSubjectID, self.currentMonth, self.showAll))

                )
            )

        for subject in self.subjects:
            self.root.get_screen('mainScreen').ids.scrollSubjectSelect.children[0].add_widget(
                ChangeGroupItem(
                    id=f"Sub{subject[0]}",
                    image=self.subjectsBg.get(str(subject[0]), "pictures/default.jpg"),
                    text=subject[1],
                    on_release=lambda x, sub = subject[0]: (self.setSelectedSubjectID(sub),
                                                            self.changeNestedScreen("editSheduleScreen", "left"),
                                                            self.showShedule()
                ))
            )

        self.root.get_screen('mainScreen').ids.scrollSubject.children[0].add_widget(
            ChangeGroupItem(
                id=f"SubReturn",
                image="pictures/return.jpg",
                text="Return",
                on_release=lambda x: self.changeNestedScreen("viewGroupScreen", "left")
            )
        )

        self.root.get_screen('mainScreen').ids.scrollSubjectSelect.children[0].add_widget(
            ChangeGroupItem(
                id=f"SubReturn",
                image="pictures/return.jpg",
                text="Return",
                on_release=lambda x: self.changeNestedScreen("manageGroupScreen", "left")
            )
        )

        for item in self.root.get_screen('mainScreen').ids.scrollGroupNested.children:
            if item.id == "areaGroupNested":
                for group in self.groups:
                    item.add_widget(ChangeGroupItem(
                        id=f"N{group[0]}",
                        image="pictures/setGroup.png",
                        text=group[1],
                        on_release=lambda x, g=group: (
                            self.setCurrentGroupID(g[0]),
                            self.changeNestedScreen("selectSubjectScreen", "left")
                        )
                    ))

        for item in self.root.get_screen('mainScreen').ids.scrollGroup.children:
            if str(item.id) == "areaGroup":
                itemID = item

                for group in self.groups:
                    item.add_widget(ChangeGroupItem(id=str(group[0]), image="pictures/setGroup.png", text=group[1],
                                                    on_release=lambda x, g=group:(
                                                    self.changeNestedScreen("manageGroupScreen", "left"),
                                                                                   self.setCurrentGroupID(g[0]))))


        itemID.add_widget(ChangeGroupItem(id="addNewGroup", image="pictures/plus.jpg",
                                          text="Add New Group",
                                          on_release=lambda x: self.changeNestedScreen(
                                                                    "addNewGroupScreen", "left")))


    def resetWidgets(self):
        for child in list(self.root.get_screen('mainScreen').ids.scrollGroup.children):
            self.root.get_screen('mainScreen').ids.scrollGroup.remove_widget(child)

        for child in list(self.root.get_screen('mainScreen').ids.scrollGroupNested.children):
            self.root.get_screen('mainScreen').ids.scrollGroupNested.remove_widget(child)

        for child in list (self.root.get_screen('mainScreen').ids.scrollSubject.children):
            self.root.get_screen('mainScreen').ids.scrollSubject.remove_widget(child)

        for child in list (self.root.get_screen('mainScreen').ids.scrollSubjectSelect.children):
            self.root.get_screen('mainScreen').ids.scrollSubjectSelect.remove_widget(child)

        self.on_start()

    def deleteGroup(self):
        try:
            db = Database()
            db.deleteGroup(self.selectedGroupID)
            db.close()

            self.resetWidgets()
            self.snackBarReGroup(self.selectedGroupID, True)
        except:
            self.snackBarReGroup(self.selectedGroupID, False)

    def getGroupCount(self):
        return self.countOfGroups

    def findWidgetByID(self, container, id):
        for widget in container.children:
            if widget.id == id:
                return widget
        return None

    def printID(self, id):
        if self.currentMark == "view":
            return
        elif self.currentMark == "clear":
            self.currentMark = ""
        else:
            custom_table = self.root.get_screen('mainScreen').ids.custom_table.ids.tableData
            cell = self.findWidgetByID(custom_table, id)
            lst = [str(i) for i in range(1, 11)]

            if (cell.text == "H1" or cell.text == 'H2') and self.currentMark in lst:
                cell.text = str(cell.text + ' / ' + self.currentMark)
                self.saveToStudents(id, cell.text)
            elif cell.text in lst and (self.currentMark == 'H1' or self.currentMark == 'H2'):
                dump = cell.text
                cell.text = self.currentMark + ' / ' + dump
                self.saveToStudents(id, cell.text)
            else:
                cell.text = self.currentMark
                self.saveToStudents(id, cell.text)

    def getWidgets(self, key, text, id=None):
        if key == 0:
            return CellStudentHead(text=text)

        elif key == 1:
            return CellHead(text=text)

        elif key == 2:
            return CellStudent(text=text, id=id)
        else:
            return CellDefaultButton(text=text, id=str(id))

    def saveToStudents(self, id, RowAttendance):
        newID = ""
        date = ""
        chars = 0
        lst = [str(i) for i in range(0, 11)]
        flg = False

        for char in id:
            if char in lst:
                newID += char
                chars += 1
            else:
                break

        date = id[chars:].lstrip("-")

        attendance = 0
        mark = 0

        if " / " in RowAttendance:
            attendancePart, markPart = RowAttendance.split(" / ")

            if markPart.isdigit():
                mark = int(markPart)
            else:
                mark = 0
        elif RowAttendance.isdigit():
            mark = int(RowAttendance)
            attendancePart = ""
        else:
            attendancePart = RowAttendance

        if attendancePart == "H1":
            attendance = 1
        elif attendancePart == "H2":
            attendance = 2
        elif attendancePart == "":
            attendance = 0

        for student in self.students:
            if student.id == int(newID):

                flg = False
                for i, (curDate, curAttendance, curMark) in enumerate(student.grades):
                    if curDate == date:
                        student.grades[i] = (curDate, attendance, mark)
                        flg = True
                        break

                if not flg:
                    student.grades.append((date, attendance, mark))
                break

    def showStudentCard(self, id):
        mainScreen = self.root.get_screen('mainScreen')
        table_float_layout = mainScreen.ids.tableFloatLayout

        if mainScreen.ids.custom_table.size_hint_x == 0.7:
            if self.studentInfo in table_float_layout.children:
                table_float_layout.remove_widget(self.studentInfo)
            mainScreen.ids.custom_table.size_hint_x = 1
        else:
            mainScreen.ids.custom_table.size_hint_x = 0.7
            self.studentInfo = StudentInfoLayout()

            for student in self.students:
                if student.id == int(id):
                    self.studentInfo.ids.studentID.text = str(student.id)
                    self.studentInfo.ids.studentLastName.text = student.lastName
                    self.studentInfo.ids.studentFirstName.text = student.firstName
                    self.studentInfo.ids.studentMiddleName.text = student.middleName
                    self.studentInfo.ids.studentPhone.text = str(student.phone)
                    self.studentInfo.ids.studentEmail.text = str(student.email)

                    stdRating, stdMissing = student.calculateAttendance()
                    self.studentInfo.ids.studentRating.text = f"{stdRating:.2f}"
                    self.studentInfo.ids.studentMissing.text = str(stdMissing)

            table_float_layout.add_widget(self.studentInfo)

    def createTable(self, groupID, subjectID, month, showAll=False):
        db = Database()
        self.students, self.countOfStudents = db.getStudents(groupID, subjectID)
        self.dates = db.getShedules(groupID, subjectID)
        db.close()

        tableData = self.root.get_screen('mainScreen').ids.custom_table.ids.tableData
        for child in list(tableData.children):
            tableData.remove_widget(child)

        studentData = self.root.get_screen('mainScreen').ids.custom_table.ids.studentData
        for child in list(studentData.children):
            studentData.remove_widget(child)

        if showAll == False:
            self.dates = [date for date in self.dates if date[0].split("-")[1] == month]

        if not self.students:
            return

        self.rowsCount = self.countOfStudents + 1
        self.columnsCount = len(self.dates)

        tableData = self.root.get_screen('mainScreen').ids.custom_table.ids.tableData
        tableData.cols = self.columnsCount
        tableData.rows = self.rowsCount

        studentData = self.root.get_screen('mainScreen').ids.custom_table.ids.studentData
        studentData.cols = 1
        studentData.rows = self.rowsCount

        studentData.add_widget(self.getWidgets(0, "Student"))

        for student in self.students:
            cell = self.getWidgets(2, student.lastName + " " + student.firstName[0] +
                                   "." + student.middleName[0] + ".", str(student.id))
            studentData.add_widget(cell)

        for head in self.dates:
            newHead = head[0].replace("-", " ").split(" ")

            newHead = newHead[2] + '.' + newHead[1] + '.' + newHead[0]

            tableData.add_widget(self.getWidgets(1, newHead))

        for student in self.students:
            for date in self.dates:
                date = date[0]
                attendance = ""
                mark = ""

                for curDate in student.grades:
                    if curDate[0] == date:
                        attendance = curDate[1]
                        mark = curDate[2]

                        if attendance == 0:
                            attendance = ""
                        elif attendance == 1:
                            attendance = "H1"
                        elif attendance == 2:
                            attendance = "H2"
                        else:
                            attendance = "error"

                        if mark == 0:
                            mark = ""

                if attendance == "" and mark == "":
                    cell = self.getWidgets(3, "", str(student.id) + "-" + date)
                elif mark == "":
                    cell = self.getWidgets(3, attendance, str(student.id) + "-" + date)
                elif attendance == "":
                    cell = self.getWidgets(3, str(mark), str(student.id) + "-" + date)
                else:
                    cell = self.getWidgets(3, attendance + " / " + str(mark), str(student.id) + "-" + date)

                tableData.add_widget(cell)

    def snackBarCopy(self, text):
        MDSnackbar(MDSnackbarText(text="Copied to clipboard successfully!"),
                   pos_hint={"center_x": 0.5, "bottom": 0.1},
                   size_hint_x=0.3,
                   radius=[20, 20, 20, 20],

                   ).open()

        clp.Clipboard.copy(text)

    def snackBarCrGroup(self, text, key):
        if key:
            MDSnackbar(MDSnackbarText(text=f"Group {text} created successfully!"),
                       pos_hint={"center_x": 0.5, "bottom": 0.1},
                       size_hint_x=0.3,
                       radius=[20, 20, 20, 20],

                       ).open()
        else:
            MDSnackbar(MDSnackbarText(text=f"Group {text} creation failed!"),
                       pos_hint={"center_x": 0.5, "bottom": 0.1},
                       size_hint_x=0.3,
                       radius=[20, 20, 20, 20],

                       ).open()

    def snackBarReGroup(self, text, key):
        if key:
            MDSnackbar(MDSnackbarText(text=f"Group {text} removed successfully!"),
                       pos_hint={"center_x": 0.5, "bottom": 0.1},
                       size_hint_x=0.3,
                       radius=[20, 20, 20, 20],

                       ).open()
        else:
            MDSnackbar(MDSnackbarText(text=f"Group {text} remove failed!"),
                       pos_hint={"center_x": 0.5, "bottom": 0.1},
                       size_hint_x=0.3,
                       radius=[20, 20, 20, 20],

                       ).open()

    def snackBarAddStudent(self, key):
        if key:
            MDSnackbar(MDSnackbarText(text=f"Student added successfully!"),
                       pos_hint={"center_x": 0.5, "bottom": 0.1},
                       size_hint_x=0.3,
                       radius=[20, 20, 20, 20],

                       ).open()
        else:
            MDSnackbar(MDSnackbarText(text=f"Student add failed!"),
                       pos_hint={"center_x": 0.5, "bottom": 0.1},
                       size_hint_x=0.3,
                       radius=[20, 20, 20, 20],

                       ).open()

    def snackBarEditStudent(self, key):
        if key:
            MDSnackbar(MDSnackbarText(text=f"Student edited successfully!"),
                       pos_hint={"center_x": 0.5, "bottom": 0.1},
                       size_hint_x=0.3,
                       radius=[20, 20, 20, 20],

                       ).open()
        else:
            MDSnackbar(MDSnackbarText(text=f"Student edite failed!"),
                       pos_hint={"center_x": 0.5, "bottom": 0.1},
                       size_hint_x=0.3,
                       radius=[20, 20, 20, 20],

                       ).open()

    def snackBarRemoveStudent(self, key):
        if key:
            MDSnackbar(MDSnackbarText(text=f"Student removed successfully!"),
                       pos_hint={"center_x": 0.5, "bottom": 0.1},
                       size_hint_x=0.3,
                       radius=[20, 20, 20, 20],

                       ).open()
        else:
            MDSnackbar(MDSnackbarText(text=f"Student remove failed!"),
                       pos_hint={"center_x": 0.5, "bottom": 0.1},
                       size_hint_x=0.3,
                       radius=[20, 20, 20, 20],

                       ).open()

    def snackBarAppend(self, key):
        if key:
            MDSnackbar(MDSnackbarText(text=f"Date created successfully!"),
                       pos_hint={"center_x": 0.5, "bottom": 0.1},
                       size_hint_x=0.3,
                       radius=[20, 20, 20, 20],

                       ).open()
        else:
            MDSnackbar(MDSnackbarText(text=f"Date creation failed!"),
                       pos_hint={"center_x": 0.5, "bottom": 0.1},
                       size_hint_x=0.3,
                       radius=[20, 20, 20, 20],

                       ).open()

    def snackBarRemoveShedule(self, key):
        if key:
            MDSnackbar(MDSnackbarText(text=f"Date removed successfully!"),
                       pos_hint={"center_x": 0.5, "bottom": 0.1},
                       size_hint_x=0.3,
                       radius=[20, 20, 20, 20],

                       ).open()
        else:
            MDSnackbar(MDSnackbarText(text=f"Date remove failed!"),
                       pos_hint={"center_x": 0.5, "bottom": 0.1},
                       size_hint_x=0.3,
                       radius=[20, 20, 20, 20],

                       ).open()

    def snackBarUpdateStudents(self, key):
        if key:
            MDSnackbar(MDSnackbarText(text=f"Students data updated successfully!"),
                       pos_hint={"center_x": 0.5, "bottom": 0.1},
                       size_hint_x=0.3,
                       radius=[20, 20, 20, 20],

                       ).open()
        else:
            MDSnackbar(MDSnackbarText(text=f"Student data update failed!"),
                       pos_hint={"center_x": 0.5, "bottom": 0.1},
                       size_hint_x=0.3,
                       radius=[20, 20, 20, 20],

                       ).open()


if __name__ == "__main__":
    Journal().run()