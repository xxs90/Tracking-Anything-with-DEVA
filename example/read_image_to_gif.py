import imageio
import os
import argparse

def create_gif(image_folder, output_gif_path, duration=0.1):
    images = [img for img in os.listdir(image_folder) if img.endswith(".png") or img.endswith(".jpg")]
    images.sort()  # Ensure the images are sorted in the correct order

    # print(len(images))
    duration = len(images)/300
    frames = []
    for image in images:
        img_path = os.path.join(image_folder, image)
        frames.append(imageio.imread(img_path))

    imageio.mimsave(output_gif_path, frames, duration=duration)


def main(id):
    os.makedirs(f'./output/{id}', exist_ok=True)
    image_folder=f'/data/su0000265/ego4d_image_clips/{id}/000000/RGB'
    output_gif_path = f'./output/{id}/animation.gif'
    create_gif(image_folder, output_gif_path)
    visualization_folder = f'./output/{id}/Visualizations'
    output_visualization_gif_path = f'./output/{id}/depth_visualization_animation.gif'
    create_gif(visualization_folder, output_visualization_gif_path)
    annotation_folder = f'./output/{id}/Annotations'
    output_annotation_gif_path = f'./output/{id}/depth_annotation_animation.gif'
    create_gif(annotation_folder, output_annotation_gif_path)
    print(f"GIF saved to {output_gif_path}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate GIFs from image sequences.')
    parser.add_argument('id', type=str, help='The unique identifier for the output folder.')

    args = parser.parse_args()
    main(args.id)