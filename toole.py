import os
import subprocess

def main():
    print("=======================================================")
    print("      TOOL TAO GHOST DURATION CHO VIDEO TIKTOK         ")
    print("=======================================================\n")

    # Di chuyển đến thư mục Movies trong bộ nhớ chung của điện thoại
    target_path = os.path.expanduser("~/storage/shared/Movies")
    
    if not os.path.exists(target_path):
        print(f"Khong tim thay thu mục {target_path}. Vui long kiem tra lai quyen bo nho!")
        return

    os.chdir(target_path)
    
    # Tạo thư mục chứa video sau khi xử lý để Thư viện điện thoại dễ nhận diện
    output_dir = "Ghost_Videos"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Quét tất cả file .mp4 trong thư mục hiện tại (trừ thư mục đầu ra)
    files = [f for f in os.listdir('.') if f.endswith('.mp4') and f != output_dir]

    if not files:
        print("Khong tim thay file .mp4 nao trong thu muc 'Movies'! Hay copy video vao do.")
        return

    print(f"Tim thay {len(files)} video. Dang tien hanh xu ly...\n")

    for filename in files:
        print(f"Dang xu ly: {filename}")
        output_path = os.path.join(output_dir, filename)
        
        # Lệnh FFmpeg chèn 24 phút thời lượng ảo từ giây thứ 50 (giữ nguyên chất lượng -c copy)
        cmd = [
            "ffmpeg", "-y", "-v", "error", "-stats",
            "-i", filename,
            "-c", "copy",
            "-bsf:a", "setts=pts='if(gte(PTS, 50/TB), PTS+24*60/TB, PTS)':dts='if(gte(DTS, 50/TB), DTS+24*60/TB, DTS)'",
            output_path
        ]
        
        # Thực thi lệnh FFmpeg
        result = subprocess.run(cmd)
        
        if result.returncode == 0:
            print(f"-> Da luu thanh cong: Movies/{output_dir}/{filename}")
        else:
            print(f"-> Loi khi xu ly file: {filename}")
            
        print("-" * 55)

    print("\nHoan thanh tat ca! Ban hay vao ung dung Thu vien / Bo suu tap anh -> Thu muc Movies -> Ghost_Videos de xem.")

if __name__ == "__main__":
    main()
