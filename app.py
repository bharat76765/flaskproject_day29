from flask import Flask, jsonify

app = Flask(__name__)

role_images = {
    "Data science": "https://pickl.ai/blog/wp-content/uploads/2023/08/Data-Science-RoadMap-programming-language.jpg",
    "Web Developer": "https://i.redd.it/pcwumc5m7zl41.jpg",
    "Database Administrator":"https://cdn.sketchbubble.com/pub/media/catalog/product/optimized1/3/f/3f40bdc058b61f0fec2e79774fd88d949e0465841ba2fff7d1b67a763e930ec7/database-administrator-dba-slide3.png",
    "Analyst":"https://media.licdn.com/dms/image/D4D22AQGcFsR6rUKf5g/feedshare-shrink_800/0/1691817966309?e=2147483647&v=beta&t=feA6Buu_npcUo9Gf2IU6xfcpiNDUvjrSO5v-rkv3-uQ",
    "Information technology management":"https://cdn.prod.website-files.com/6514c506ba80b4a13f75decd/65d38104e2f6050782bd4357_develop%20a%20technology%20roadmap%2001.png",
    "Application Developer":"https://redblink.com/wp-content/uploads/2020/09/android-mobile-app-development-roadmap.png",
    "Software Architect":"https://roadmap.sh/og/roadmap/software-architect",
    "DevOps Engineer":"https://i.pinimg.com/1200x/c9/ee/30/c9ee301b0f16542cbebe9d9af125d30d.jpg",
    "Data Engineer":"https://www.odinschool.com/hs-fs/hubfs/Data%20Engineer%20Roadmap.webp?width=1100&height=768&name=Data%20Engineer%20Roadmap.webp",
    "Java Developer":"https://copyassignment.com/wp-content/uploads/2022/11/Roadmap.jpg",
    "Network administrator":"https://www.freecodecamp.org/news/content/images/2020/08/certification-roadmap.jpg",
    "Software engineer":"https://media.licdn.com/dms/image/D4D22AQE9pgvUvaj7JA/feedshare-shrink_800/0/1696387382560?e=2147483647&v=beta&t=bKRT_Sg374itFPWn1enzIyrayZQEj9BWwWfP5CA0T6A",
    "Full stack developer":"https://i.pinimg.com/originals/78/87/61/78876171ebe3d4a5013d2ee894c2d10c.jpg",
    "Information Security Analysts":"https://www.collidu.com/media/catalog/product/img/8/e/8ed5d31076a7fd8892431fa97321d84a94d36e5d4dafbafc7ccb86e32a5d8f14/cybersecurity-roadmap-slide1.png",
    "Product Management":"https://venngage-wordpress.s3.amazonaws.com/uploads/2023/09/internal-1024x791.png",
    "Cloud Engineer":"https://training.linuxfoundation.org/wp-content/uploads/2021/07/Cloud-Roadmap.png",
    "Blockchain Engineer":"https://roadmap.sh/og/roadmap/blockchain",
}
@app.route('/')
def index():
    return "API ready for service"
@app.route('/api/roadmap/<role>', methods=['GET'])
def get_roadmap(role):
    image_url = role_images.get(role)
    if image_url:
        return jsonify({"role": role, "image_url": image_url})
    else:
        return jsonify({"error": "Role not found"}), 404

if __name__ == '__main__':
    app.run(debug=True, port=5050)
