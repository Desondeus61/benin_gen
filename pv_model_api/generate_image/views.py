from rest_framework import views, response
from diffusers import DiffusionPipeline
import torch
pipe = DiffusionPipeline.from_pretrained("stabilityai/stable-diffusion-xl-base-1.0", torch_dtype=torch.float16, use_safetensors=True, variant="fp16")
class ImageGenerationView(views.APIView):
    def post(self, request):
        prompt = request.data.get('prompt', '')
        # # Générer l'image à partir du prompt
        images = pipe(prompt=prompt).images[0]
        # Retourner l'image générée
        return response.Response({'image': images})

