import torch
import transformers
from transformers import AutoModelForCausalLM, AutoTokenizer

model = "tiiuae/falcon-7b"

tokenizer = AutoTokenizer.from_pretrained(model)
pipeline = transformers.pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    torch_dtype=torch.bfloat16,
    trust_remote_code=True,
    device_map="auto",
)
sequences = pipeline(
    [
        """from this context : Once upon a time, in the small town of Willowbrook, there lived a curious young girl named Emily. 
    With her bright eyes and an insatiable thirst for adventure, she was always seeking new experiences and discoveries.
    One sunny morning, Emily ventured into the dense forest that surrounded her town. 
    She had heard tales of a hidden waterfall deep within the woods, and her heart was set on finding it. 
    Armed with her trusty backpack and a sense of determination, she followed a faint trail leading her deeper into the wilderness.
    As she walked, Emily noticed the forest changing around her. The air grew cooler, 
    and beams of sunlight filtered through the thick canopy of leaves, creating a magical ambiance. 
    She could hear the soft chirping of birds and the rustling of leaves under her feet. 
    It felt as though nature itself was guiding her towards her destination.
    After hours of hiking, Emily's perseverance paid off. She stumbled upon a hidden clearing bathed in golden sunlight. 
    In the center stood a majestic waterfall, 
    cascading down from the rocks above into a crystal-clear pool below. The sight was breathtaking, 
    and Emily couldn't help but be in awe of its beauty.
    answer this question : where did emily live ?
    answer :""",
        "hello",
    ],
    max_new_tokens=10,
    do_sample=True,
    top_k=10,
    temperature=3e-4,
    num_return_sequences=1,
    eos_token_id=tokenizer.eos_token_id,
    return_full_text=False,
)
outputs = [seq["generated_text"] for seq in sequences[0]]
print(outputs)
