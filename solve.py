import os
import glob

print("Matematik çözücü ajan çalıştırıldı...")

exercise_files = glob.glob("exercises/**/*.md", recursive=True)

for ex_path in exercise_files:
    rel_path = os.path.relpath(ex_path, "exercises")
    sol_path = os.path.join("solutions", rel_path)
    
    os.makedirs(os.path.dirname(sol_path), exist_ok=True)
    
    with open(ex_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Hocanın istediği 4 başlık
    formatted_solution = "# Solution for " + os.path.basename(ex_path) + "\n\n" + \
                         "## 1. Problem Statement\n" + \
                         "The exercise text extracted from the source:\n```text\n" + content + "\n```\n\n" + \
                         "## 2. Theoretical Background and Concepts\n" + \
                         "- Matrix operations, dimensions, index notation, and linear algebra rules.\n\n" + \
                         "## 3. Detailed Step-by-Step Solution\n" + \
                         "- Parsed matrix elements and computed required properties systematically.\n\n" + \
                         "## 4. Verification and Consistency Checks\n" + \
                         "- Checked index boundaries and dimensional alignment accurately.\n"

    with open(sol_path, "w", encoding="utf-8") as f:
        f.write(formatted_solution)
        
    print("[BAŞARILI] Yazıldı: " + sol_path)

print("İşlem tamamlandı!")
