import os
import random
import shutil

def split_and_move_images(source_dir_fish, source_dir_noFish, dest_dir,
                          train_ratio=0.7, val_ratio=0.15, test_ratio=0.15,
                          seed=42):
    """
    Flytter bilder fra to kildemapper (Fish og NoFish) til trenings-, validerings-
    og testmapper, i forholdet 70/15/15. Skriptet fjerner bildene fra kildemappene,
    siden det bruker shutil.move().
    """

    # Sett en fast seed for å reprodusere samme random-split hver gang
    random.seed(seed)
    
    # 1) Opprett undermapper for train/val/test/fish/noFish
    train_fish_dir = os.path.join(dest_dir, 'train', 'fish')
    train_noFish_dir = os.path.join(dest_dir, 'train', 'noFish')
    val_fish_dir   = os.path.join(dest_dir, 'val', 'fish')
    val_noFish_dir = os.path.join(dest_dir, 'val', 'noFish')
    test_fish_dir  = os.path.join(dest_dir, 'test', 'fish')
    test_noFish_dir= os.path.join(dest_dir, 'test', 'noFish')

    # Opprett mappene hvis de ikke eksisterer fra før
    for d in [train_fish_dir, train_noFish_dir,
              val_fish_dir, val_noFish_dir,
              test_fish_dir, test_noFish_dir]:
        os.makedirs(d, exist_ok=True)
    
    # 2) Funksjon for å splitte og flytte for EN klasse (f.eks. 'fish' eller 'noFish')
    def split_class_images(source_dir, train_dir, val_dir, test_dir,
                           train_ratio, val_ratio, test_ratio):
        """
        Leser alle filer i source_dir, randomiserer rekkefølgen,
        beregner antall til train/val/test, og flytter så filene.
        """
        # Finn alle bilder (her regnet med f.eks. .jpg, .png, .jpeg etc.)
        valid_extensions = ('.jpg', '.jpeg', '.png', '.bmp')
        all_files = [f for f in os.listdir(source_dir)
                     if f.lower().endswith(valid_extensions)]
        
        total = len(all_files)
        print(f"[INFO] Fant {total} bilder i '{source_dir}'")
        
        # Randomiser listen
        random.shuffle(all_files)
        
        # Beregn antall bilder i hver del
        train_count = int(total * train_ratio)
        val_count   = int(total * val_ratio)
        test_count  = total - train_count - val_count  # Resten
        
        # Split listene
        train_files = all_files[:train_count]
        val_files   = all_files[train_count:train_count + val_count]
        test_files  = all_files[train_count + val_count:]
        
        # Flytt filene
        for f in train_files:
            src_path = os.path.join(source_dir, f)
            dst_path = os.path.join(train_dir, f)
            shutil.move(src_path, dst_path)
        
        for f in val_files:
            src_path = os.path.join(source_dir, f)
            dst_path = os.path.join(val_dir, f)
            shutil.move(src_path, dst_path)
        
        for f in test_files:
            src_path = os.path.join(source_dir, f)
            dst_path = os.path.join(test_dir, f)
            shutil.move(src_path, dst_path)
        
        print(f"[INFO] Flyttet {len(train_files)} treningsfiler, "
              f"{len(val_files)} valideringsfiler, "
              f"{len(test_files)} testfiler fra '{source_dir}'.\n")
    
    # 3) Split og flytt for 'Fish'
    split_class_images(source_dir_fish, train_fish_dir, val_fish_dir, test_fish_dir,
                       train_ratio, val_ratio, test_ratio)
    
    # 4) Split og flytt for 'NoFish'
    split_class_images(source_dir_noFish, train_noFish_dir, val_noFish_dir, test_noFish_dir,
                       train_ratio, val_ratio, test_ratio)


if __name__ == "__main__":
    # Eksempelstier (juster disse så de samsvarer med dine lokale stier)
    source_dir_fish   = r"C:\Users\lotte\Programmering og koding\IDATG2206 - computer vision\Fish-detection\AnadromSmall\Fish"
    source_dir_noFish = r"C:\Users\lotte\Programmering og koding\IDATG2206 - computer vision\Fish-detection\AnadromSmall\NoFish"
    
    # Denne mappen vil inneholde under-mapper for train/val/test
    dest_dir          = r"C:\Users\lotte\Programmering og koding\IDATG2206 - computer vision\Fish-detection\dataset"
    
    # Kjør funksjonen med default-forhold 70/15/15
    split_and_move_images(source_dir_fish, source_dir_noFish, dest_dir)
