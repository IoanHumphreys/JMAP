import customtkinter
from tkinter import filedialog
from tkinter import messagebox
import configparser
from PIL import Image
import json
import os
import datetime

# Define paths
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

def read_config():
    config = configparser.ConfigParser()
    config.read('shared/config.ini') 
    return config

def save_config(config):
    with open('shared/config.ini', 'w') as configfile:
        config.write(configfile)

def update_directory(entry, config_key):
    directory = filedialog.askdirectory(initialdir=SCRIPT_DIR)
    if directory: 
        entry.delete(0, customtkinter.END) 
        entry.insert(0, directory)
        config = read_config()
        if not config.has_section('Paths'):
            config.add_section('Paths')
        config.set('Paths', config_key, directory) 
        save_config(config) 

def update_inputs_folder():
    try:
        update_directory(inputs_folder_entry, 'inputs_folder')
    except Exception as e:
        messagebox.showerror("Error", f"Failed to update inputs directory: {e}")

def update_outputs_folder():
    try:
        update_directory(outputs_folder_entry, 'outputs_folder')
    except Exception as e:
        messagebox.showerror("Error", f"Failed to update outputs directory: {e}")

def update_fmodel_folder():
    try:
        update_directory(fmodel_folder_entry, 'fmodel_folder')
    except Exception as e:
        messagebox.showerror("Error", f"Failed to update fmodel directory: {e}")

def show_poi_frame():
    poi_frame.grid()
    settings_frame.grid_remove()

def show_settings_frame():
    settings_frame.grid() 
    poi_frame.grid_remove() 

def generate_converted_json():
    try:
        process_json_files()
        messagebox.showinfo("Success", "The JSON files have been successfully converted.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred during the conversion: {str(e)}")

# Setup App 
app = customtkinter.CTk(fg_color='#111112')
app.geometry("1150x670")
app.title("JMAP stable 1.0.0 - Alpha")

# Grid Layout
app.grid_columnconfigure(1, weight=1)
app.grid_columnconfigure((2, 3), weight=0)
app.grid_rowconfigure((0, 1, 2), weight=1)

# Sidebar frame
sidebar_frame = customtkinter.CTkFrame(app, corner_radius=0, fg_color="#151517")
sidebar_frame.grid(row=0, column=0, rowspan=7, sticky="nsew")
sidebar_frame.grid_rowconfigure(7, weight=1)
side_bar_text = customtkinter.CTkFont(family="Poppins", size=14, weight="normal")
side_bar_buttons = customtkinter.CTkFont(family="Poppins", size=13, weight="bold")

# Define logo image
logo_image = customtkinter.CTkImage(light_image=Image.open("cache/icons/jmap_logo.png"), size=(80, 80))

# Create logo label
logo_label = customtkinter.CTkLabel(sidebar_frame, text="", image=logo_image)
logo_label.grid(row=0, column=0, padx=10, pady=10)

poi_image = customtkinter.CTkImage(light_image=Image.open("cache/icons/poi_import.png"), size=(20, 20))
import_poi = customtkinter.CTkButton(sidebar_frame, font=side_bar_text, image=poi_image, anchor="w", text="POI", height=40, width=220, fg_color="#252529", hover_color="#34343C", command=show_poi_frame)
import_poi.grid(row=1, column=0, padx=20, pady=10, sticky="w")

ui_image = customtkinter.CTkImage(light_image=Image.open("cache/icons/ui_import.png"), size=(20, 20))
import_ui = customtkinter.CTkButton(sidebar_frame, fg_color="transparent", font=side_bar_text, image=ui_image, anchor="w", text="UI Widgets", height=40, width=220, hover_color="#252529")
import_ui.grid(row=2, column=0, padx=20, pady=10, sticky="w")

audio_image = customtkinter.CTkImage(light_image=Image.open("cache/icons/audio_import.png"), size=(20, 20))
import_audio = customtkinter.CTkButton(sidebar_frame, fg_color="transparent", font=side_bar_text, image=audio_image, anchor="w", text="Audio", height=40, width=220, hover_color="#252529")
import_audio.grid(row=3, column=0, padx=20, pady=10, sticky="w")

texture_data_image = customtkinter.CTkImage(light_image=Image.open("cache/icons/texture_data_input.png"), size=(20, 20))
texture_data = customtkinter.CTkButton(sidebar_frame, fg_color="transparent", font=side_bar_text, image=texture_data_image, anchor="w", text="Texture Data", height=40, width=220, hover_color="#252529")
texture_data.grid(row=4, column=0, padx=20, pady=10, sticky="w")

vertex_color_image = customtkinter.CTkImage(light_image=Image.open("cache/icons/vertex_color_import.png"), size=(20, 20))
vertex_colors = customtkinter.CTkButton(sidebar_frame, fg_color="transparent", font=side_bar_text, image=vertex_color_image, anchor="w", text="Vertex Colors", height=40, width=220, hover_color="#252529")
vertex_colors.grid(row=5, column=0, padx=20, pady=10, sticky="w")

pp_import_image = customtkinter.CTkImage(light_image=Image.open("cache/icons/post_processing_import.png"), size=(20, 20))
pp_import = customtkinter.CTkButton(sidebar_frame, fg_color="transparent", font=side_bar_text, image=pp_import_image, anchor="w", text="Post Processing", height=40, width=220, hover_color="#252529")
pp_import.grid(row=6, column=0, padx=20, pady=10, sticky="w")

combine_files_image = customtkinter.CTkImage(light_image=Image.open("cache/icons/combine_files.png"), size=(20, 20))
combine_files = customtkinter.CTkButton(sidebar_frame, fg_color="transparent", font=side_bar_text, image=combine_files_image, anchor="w", text="Combine Files", height=40, width=220, hover_color="#252529")
combine_files.grid(row=7, column=0, padx=20, pady=10, sticky="w")

# Additional buttons
support_button_image = customtkinter.CTkImage(light_image=Image.open("cache/icons/support_button.png"), size=(20, 20))
support = customtkinter.CTkButton(sidebar_frame, fg_color="#252529", font=side_bar_buttons, text="Support", height=40, width=220, hover_color="#202024", image=support_button_image)
support.grid(row=9, column=0, padx=20, pady=(10, 10))

settings_button_image = customtkinter.CTkImage(light_image=Image.open("cache/icons/settings_button.png"), size=(20, 20))
settings_button = customtkinter.CTkButton(sidebar_frame, fg_color="#252529", font=side_bar_buttons, text="Settings", height=40, width=220, hover_color="#202024", image=settings_button_image, command=show_settings_frame)
settings_button.grid(row=10, column=0, padx=20, pady=(10, 20))

# Headings
title_font = customtkinter.CTkFont(family="Poppins", size=20, weight="bold")
sub_title_font = customtkinter.CTkFont(family="Poppins", size=15, weight="bold")

# POI Frame Setup
poi_frame = customtkinter.CTkFrame(app, corner_radius=0, fg_color="transparent")
poi_frame.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)
poi_frame.columnconfigure(0, weight=1)

# POI Title
poi_label = customtkinter.CTkLabel(poi_frame, text="Import POI", font=title_font)
poi_label.grid(row=1, column=0, padx=30, pady=40, sticky="w")

# POI Generate Button
poi_btn_font = customtkinter.CTkFont(family="Poppins", size=14, weight="normal")
poi_generate = customtkinter.CTkButton(poi_frame, text="Generate Files", hover_color="#06B66B", fg_color="#029556", border_width=0, text_color="#C9FFE8", height=35, font=poi_btn_font, command=generate_converted_json)
poi_generate.grid(row=2, column=0, padx=30, pady=10, sticky="w")

# Settings
settings_frame = customtkinter.CTkFrame(app, corner_radius=0, fg_color="transparent")
settings_frame.grid(row=0, column=1, sticky="nsew")
settings_frame.columnconfigure(0, weight=1)
settings_frame.grid_remove()

directoriesLabel = customtkinter.CTkLabel(settings_frame, text="Directories", font=title_font)
directoriesLabel.grid(row=1, column=0, padx=30, pady=40, sticky="w")

change_button_img = customtkinter.CTkImage(light_image=Image.open("cache/icons/folder_icon.png"), size=(20, 20))

directoriesLabel = customtkinter.CTkLabel(settings_frame, text="Directories", font=title_font)
directoriesLabel.grid(row=1, column=0, padx=30, pady=40, sticky="w")

change_button_img = customtkinter.CTkImage(light_image=Image.open("cache/icons/folder_icon.png"), size=(20, 20))

inputs_folder = customtkinter.CTkLabel(settings_frame, text="Inputs*", font=sub_title_font)
inputs_folder.grid(row=2, column=0, padx=30, pady=5, sticky="w")
inputs_folder_entry = customtkinter.CTkEntry(settings_frame, placeholder_text="Inputs Folder", border_width=0, fg_color="#09090A")
inputs_folder_entry.grid(row=3, column=0, padx=(30, 2), pady=(1, 20), sticky="ew")
inputs_change_button = customtkinter.CTkButton(settings_frame, text="", image=change_button_img, hover_color="#202024", fg_color="#09090A", border_width=0, text_color="#A1A1A1", width=5, command=update_inputs_folder)
inputs_change_button.grid(row=3, column=2, padx=7, pady=(1, 20), sticky="ew")

fmodel_folder_label = customtkinter.CTkLabel(settings_frame, text="FModel JSON (optional)", font=sub_title_font)
fmodel_folder_label.grid(row=4, column=0, padx=30, pady=5, sticky="w")
fmodel_folder_entry = customtkinter.CTkEntry(settings_frame, placeholder_text="FModel (optional)", border_width=0, fg_color="#09090A")
fmodel_folder_entry.grid(row=5, column=0, padx=(30, 2), pady=(1, 20), sticky="ew")
fmodel_change_button = customtkinter.CTkButton(settings_frame, text="", image=change_button_img, hover_color="#202024", fg_color="#09090A", border_width=0, text_color="#A1A1A1", width=5, command=update_fmodel_folder)
fmodel_change_button.grid(row=5, column=2, padx=7, pady=(1, 20), sticky="ew")

outputs_folder_label = customtkinter.CTkLabel(settings_frame, text="Outputs*", font=sub_title_font)
outputs_folder_label.grid(row=6, column=0, padx=30, pady=5, sticky="w")
outputs_folder_entry = customtkinter.CTkEntry(settings_frame, placeholder_text="Path", border_width=0, fg_color="#09090A")
outputs_folder_entry.grid(row=7, column=0, padx=(30, 2), pady=(1, 20), sticky="ew")
outputs_change_button = customtkinter.CTkButton(settings_frame, text="", image=change_button_img, hover_color="#202024", fg_color="#09090A", border_width=0, text_color="#A1A1A1", width=5, command=update_outputs_folder)
outputs_change_button.grid(row=7, column=2, padx=7, pady=(1, 20), sticky="ew")

otherLabel = customtkinter.CTkLabel(settings_frame, text="Other", font=title_font)
otherLabel.grid(row=8, column=0, padx=30, pady=40, sticky="w")

def checkbox_event():
    print("checkbox toggled, current value:", check_var.get())

checkbox_font = customtkinter.CTkFont(family="Poppins", size=13, weight="bold")
check_var = customtkinter.StringVar(value="on")
checkbox = customtkinter.CTkCheckBox(settings_frame, fg_color="#09090A", hover_color="#202024", text="Developer Mode", font=checkbox_font, border_width=2, command=checkbox_event, variable=check_var, onvalue="on", offvalue="off", checkbox_width=20, checkbox_height=20)
checkbox.grid(row=9, column=0, padx=30, pady=5, sticky="w")

# Keep these here
config = read_config()
inputs_path = config.get('Paths', 'inputs_folder', fallback='Select inputs directory')
outputs_path = config.get('Paths', 'outputs_folder', fallback='Select outputs directory')
fmodel_path = config.get('Paths', 'fmodel_folder', fallback='Select fmodel directory')
inputs_folder_entry.insert(0, inputs_path)
outputs_folder_entry.insert(0, outputs_path)
fmodel_folder_entry.insert(0, fmodel_path)

# Utility functions
def format_value(value):
    return f"{value:.1f}" if isinstance(value, float) else value

# Format 3D Values
def format_relative_data(data, key):
    relative_data = data.get(key, {})
    
    if key == 'RelativeLocation':
        default_value = {'X': 0.0, 'Y': 0.0, 'Z': 0.0}
    elif key == 'RelativeRotation':
        default_value = {'Pitch': 0.0, 'Yaw': 0.0, 'Roll': 0.0}
    elif key == 'RelativeScale3D':
        default_value = {'X': 1.0, 'Y': 1.0, 'Z': 1.0}
    else:
        default_value = {}
    
    if (key != 'RelativeScale3D' and all(value == 0.0 for value in relative_data.values())) or \
            (key == 'RelativeScale3D' and all(value == 1.0 for value in relative_data.values())):
        return ""

    # Format non-zero or non-one values
    formatted_data = f"{key}=({', '.join(f'{k}={format_value(relative_data.get(k, default_value.get(k, 0.0)))}' for k in default_value.keys())})"
    return formatted_data

# Convert Data
def convert_to_game_engine_format(data):
    output = "Begin Map\n    Begin Level\n\n"

    # First Table
    first_table_name = data[0].get('Name', '') if data else ''

    for entry_index, entry in enumerate(data):
        template = entry.get('Template', {})
        properties = entry.get('Properties', {})

        # Check if both RelativeLocation and RelativeRotation are zero
        if all(value == 0.0 for value in properties.get('RelativeLocation', {}).values()) and \
                all(value == 0.0 for value in properties.get('RelativeRotation', {}).values()):
            continue

        # Template
        template_obj_name = template.get('ObjectName', '').split("Default__", 1)[-1].split(":")[0].rstrip('_').rstrip("'")
        template_obj_path = template.get('ObjectPath', '').replace('FortniteGame/Content', '/Game').rstrip('0123456789')
        obj_path = template_obj_path + template_obj_name if template_obj_name else "/Script/FortniteGame.FortStaticMeshActor"

        # Static Mesh
        static_mesh_info = properties.get('StaticMesh', {})
        static_mesh_name = static_mesh_info.get('ObjectName', '').split("StaticMesh'", 1)[-1].split(":")[0].rstrip('_').rstrip("'") if isinstance(static_mesh_info, dict) else ''
        static_mesh_path = static_mesh_info.get('ObjectPath', '').replace('FortniteGame/Content', '/Game').rstrip('0123456789') if isinstance(static_mesh_info, dict) else ''

        # Override Materials
        override_materials_info = properties.get('OverrideMaterials', [])
        
        override_materials_paths = []
        if override_materials_info:
            for mat_info in override_materials_info:
                if mat_info:
                    mat_name = mat_info.get('ObjectName', '').split("MaterialInstanceConstant'", 1)[-1].split("'")[0]
                    mat_path = mat_info.get('ObjectPath', '').replace('FortniteGame/Content', '/Game').rstrip('0123456789')
                    override_materials_paths.append(mat_path + mat_name)
        
        actor_text = f"        Begin Actor Class={obj_path}\n" 
        actor_text += f"            Begin Object Name=\"StaticMeshComponent0\"\n"
        actor_text += f"                StaticMesh={static_mesh_path + static_mesh_name}\n"
        
        if override_materials_paths:
            actor_text += "                OverrideMaterials(0)="
            for mat_path in override_materials_paths:
                actor_text += f"\"{mat_path}\", "
            actor_text = actor_text[:-2] 
            actor_text += "\n"

        for key in ['RelativeLocation', 'RelativeRotation', 'RelativeScale3D']:
            formatted_data = format_relative_data(properties, key)
            if formatted_data:
                actor_text += f"                {formatted_data}\n"

        # Vertex Colors
        if 'LODData' in entry:
            for lod_index, lod_data in enumerate(entry['LODData']):
                if 'OverrideVertexColors' in lod_data:
                    num_vertices = lod_data['OverrideVertexColors']['NumVertices']
                    vertex_colors_data = ",".join(lod_data['OverrideVertexColors']['Data'])
                    actor_text += f"                CustomProperties CustomLODData LOD={lod_index} ColorVertexData({num_vertices})= ({vertex_colors_data})\n"

        actor_text += "            End Object\n"
        actor_text += "            FortFXCustomization=\"FortFXCustomization\"\n"
        actor_text += "            BoxComponent=\"BoundingBoxComponent\"\n"
        actor_text += "            EditorOnlyStaticMeshComponent=\"EditorOnlyStaticMeshComponent\"\n"
        actor_text += f"            StaticMeshComponent=StaticMeshComponent0\n"
        actor_text += f"            RootComponent=StaticMeshComponent0\n"
        actor_text += f"            ActorLabel=\"{entry.get('Outer', '')}\"\n"
        actor_text += f"            FolderPath={first_table_name}\n" 
        actor_text += "        End Actor\n\n"

        # Exclude ignored components
        #for word in ignored_components:
            #actor_text = actor_text.replace(f"{word}'", "")

        # Exclude ignored props
       # for prop in ignored_props:
            #if prop in actor_text:
                #actor_text = ""
                #break
            
        # Remove Duplicates
        #if entry.get('Outer', '') == 'PersistentLevel':
            #continue

        output += actor_text

    output += "    End Level\n\nBegin Surface\nEnd Surface\nEnd Map\n\n"
    return output

def process_json_files():
    config = read_config()
    # Read directories from config
    inputs_dir = config.get('Paths', 'inputs_folder', fallback=SCRIPT_DIR)
    fmodel_dir = config.get('Paths', 'fmodel_folder', fallback='')
    output_base_dir = config.get('Paths', 'outputs_folder', fallback=os.path.join(SCRIPT_DIR, 'shared/outputs'))

    # Ensure the output directory exists
    if not os.path.exists(output_base_dir):
        os.makedirs(output_base_dir)

    # Process both inputs and fmodel directories
    for directory in [inputs_dir, fmodel_dir]:
        for root, dirs, files in os.walk(directory):
            for file in files:
                if file.endswith(".json"):
                    process_json_file(root, file, output_base_dir)

def process_json_file(root, file, output_base_dir):
    json_path = os.path.join(root, file)
    try:
        with open(json_path, 'r') as json_file:
            data = json.load(json_file)

        if data:
            first_item = data[0]
            template = first_item.get('Template', {})
            object_path = template.get('ObjectPath', '')
            path_parts = object_path.split('/')

            if len(path_parts) > 3:
                directory_name = path_parts[2] + "/POI"
            else:
                directory_name = "Misc"

            full_output_dir = os.path.join(output_base_dir, directory_name)
            os.makedirs(full_output_dir, exist_ok=True)

            output_file_path = os.path.join(full_output_dir, f"{os.path.splitext(file)[0]}_jmap.txt")

            converted_data = convert_to_game_engine_format(data)

            with open(output_file_path, 'w') as output_file:
                output_file.write(converted_data)

    except Exception as e:
        print(f"Error processing {json_path}: {e}")

app.mainloop()