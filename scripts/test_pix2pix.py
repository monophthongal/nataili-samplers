import uuid

from PIL import Image

from nataili.model_manager.compvis import CompVisModelManager
from nataili.stable_diffusion.compvis import CompVis
from nataili.util.logger import logger

init_image = Image.open(
    "./test_images/00726-2641044396_cute_girl_holding_a_giant_NVIDIA_gtx_1080ti_GPU_graphics_card,_Anime_Blu-Ray_boxart,_super_high_detail,_pixiv_trending.png"
).convert("RGB")

mm = CompVisModelManager()

model = "pix2pix"

mm.load(model)


output_dir = f"./test_output/{str(uuid.uuid4())}"

prompt = "make the girl a brunette"

compvis = CompVis(
    model=mm.loaded_models[model],
    model_name=model,
    output_dir=output_dir,
    disable_voodoo=True,
)
compvis.generate(
    prompt,
    init_img=init_image,
)
