from flask import Flask, render_template_string, request, jsonify

app = Flask(__name__)

# الهيكل المتطور للمصفوفة المعرفية
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>DAWAWIN v14.1 | THE GLOBAL INTELLIGENCE MATRIX</title>
    <link href="https://fonts.googleapis.com/css2?family=Amiri:wght@700&family=Inter:wght@300;400;600&family=Cairo:wght@200;400;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        :root {
            --bg: #050505;
            --accent: #d4af37;
            --text: #e0e0e0;
            --glass: rgba(255, 255, 255, 0.03);
            --border: rgba(212, 175, 55, 0.2);
        }

        * { margin: 0; padding: 0; box-sizing: border-box; cursor: none !important; }

        body {
            background: var(--bg);
            color: var(--text);
            font-family: 'Inter', 'Cairo', sans-serif;
            overflow: hidden;
            height: 100vh;
        }

        /* Matrix Canvas */
        #matrix-canvas {
            position: fixed;
            top: 0; left: 0;
            z-index: -1;
        }

        /* Custom Cursor */
        #cursor {
            position: fixed;
            width: 8px; height: 8px;
            background: var(--accent);
            border-radius: 50%;
            pointer-events: none;
            z-index: 9999;
        }
        #cursor-follower {
            position: fixed;
            width: 30px; height: 30px;
            border: 1px solid var(--accent);
            border-radius: 50%;
            pointer-events: none;
            z-index: 9998;
            transition: transform 0.1s linear;
            mix-blend-mode: difference;
        }

        /* Main Dashboard Header */
        header {
            padding: 2rem 5%;
            text-align: center;
            animation: fadeIn 2s ease;
        }
        header h1 {
            font-family: 'Amiri', serif;
            font-size: 3.5rem;
            color: var(--accent);
            text-shadow: 0 0 20px rgba(212, 175, 55, 0.4);
            letter-spacing: 5px;
        }
        header p {
            font-size: 0.7rem;
            letter-spacing: 3px;
            opacity: 0.6;
            margin-top: 5px;
        }

        /* Bento Matrix Grid */
        .bento-grid {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            grid-template-rows: repeat(3, 180px);
            gap: 15px;
            padding: 0 5% 5% 5%;
            max-width: 1400px;
            margin: 0 auto;
        }

        .node {
            background: var(--glass);
            border: 1px solid var(--border);
            border-radius: 20px;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            transition: 0.4s cubic-bezier(0.4, 0, 0.2, 1);
            position: relative;
            overflow: hidden;
            backdrop-filter: blur(10px);
        }

        .node:hover {
            transform: translateY(-5px) scale(1.02);
            border-color: var(--accent);
            background: rgba(212, 175, 55, 0.05);
            box-shadow: 0 10px 30px rgba(0,0,0,0.5);
        }

        .node i { font-size: 2rem; color: var(--accent); margin-bottom: 15px; }
        .node h3 { font-size: 1rem; font-weight: 400; }

        /* Bento Variations */
        .cell-main { grid-column: span 2; grid-row: span 2; }
        .cell-wide { grid-column: span 2; }
        .cell-tall { grid-row: span 2; }
        .cell-gold { border-color: var(--accent); }

        /* Omni Slider Panel */
        #omni-slider {
            position: fixed;
            top: 0; right: -100%;
            width: 100%; height: 100%;
            background: rgba(5,5,5,0.95);
            backdrop-filter: blur(30px);
            z-index: 2000;
            transition: 0.6s cubic-bezier(0.77, 0, 0.175, 1);
            padding: 5%;
            overflow-y: auto;
        }
        #omni-slider.active { right: 0; }

        .close-btn {
            position: absolute; top: 30px; left: 30px;
            font-size: 2rem; color: var(--accent);
        }

        /* Forms */
        .publish-form {
            display: grid;
            gap: 20px;
            max-width: 600px;
            margin: 2rem auto;
        }
        .publish-form input, .publish-form select {
            padding: 15px;
            background: rgba(255,255,255,0.05);
            border: 1px solid var(--border);
            color: white;
            border-radius: 10px;
            font-family: 'Cairo';
        }
        .btn-submit {
            background: var(--accent);
            color: var(--bg);
            padding: 15px;
            border: none;
            border-radius: 10px;
            font-weight: bold;
        }

        @keyframes fadeIn { from { opacity: 0; } to { opacity: 1; } }

        footer {
            position: fixed; bottom: 20px; width: 100%;
            display: flex; justify-content: space-around;
            font-size: 0.7rem; opacity: 0.4;
        }
    </style>
</head>
<body>

<canvas id="matrix-canvas"></canvas>
<div id="cursor"></div>
<div id="cursor-follower"></div>

<header>
    <h1>DAWAWIN</h1>
    <p>THE GLOBAL INTELLIGENCE MATRIX • EST 2026</p>
</header>

<div class="bento-grid">
    <div class="node cell-main" onclick="openNode('خزانة الكتب الشاملة')">
        <i class="fa-solid fa-vault"></i>
        <h3>خزانة الكتب الشاملة</h3>
    </div>
    <div class="node cell-gold" onclick="openNode('الدراسات العليا')">
        <i class="fa-solid fa-graduation-cap"></i>
        <h3>الدراسات العليا</h3>
    </div>
    <div class="node" onclick="openNode('البحوث العلمية')">
        <i class="fa-solid fa-microscope"></i>
        <h3>البحوث العلمية</h3>
    </div>
    <div class="node cell-wide" onclick="openNode('المقالات الدولية')">
        <i class="fa-solid fa-globe"></i>
        <h3>المقالات الدولية</h3>
    </div>
    <div class="node cell-tall" onclick="showPublish()">
        <i class="fa-solid fa-feather"></i>
        <h3>انشر محتواك</h3>
    </div>
    <div class="node" onclick="openNode('الأرشيف التاريخي')">
        <i class="fa-solid fa-box-archive"></i>
        <h3>الأرشيف</h3>
    </div>
    <div class="node" onclick="openNode('الهوية والرسالة')">
        <i class="fa-solid fa-eye"></i>
        <h3>الهوية والرسالة</h3>
    </div>
</div>

<div id="omni-slider">
    <div class="close-btn" onclick="closeNode()"><i class="fa-solid fa-xmark"></i></div>
    <h1 id="omniTitle" style="font-family: Amiri; color: var(--accent); font-size: 3rem;"></h1>
    <div id="omniContent"></div>
</div>

<footer>
    <div>LEGAL NODE: PRIVACY • CYBER SECURITY</div>
    <div style="opacity: 0.1;">v14.1.0 STABLE BY NETIZEN</div>
    <div>COMMUNICATION: WHATSAPP • E-MAIL</div>
</footer>

<script>
    // Matrix Background
    const canvas = document.getElementById('matrix-canvas');
    const ctx = canvas.getContext('2d');
    let dots = [];
    
    function initCanvas() {
        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;
        dots = [];
        for(let i=0; i<500; i++) {
            dots.push({
                x: Math.random() * canvas.width,
                y: Math.random() * canvas.height,
                vx: (Math.random() - 0.5) * 0.5,
                vy: (Math.random() - 0.5) * 0.5
            });
        }
    }

    function animate() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        ctx.fillStyle = 'rgba(212, 175, 55, 0.3)';
        dots.forEach(d => {
            d.x += d.vx; d.y += d.vy;
            if(d.x < 0 || d.x > canvas.width) d.vx *= -1;
            if(d.y < 0 || d.y > canvas.height) d.vy *= -1;
            ctx.beginPath();
            ctx.arc(d.x, d.y, 1, 0, Math.PI*2);
            ctx.fill();
        });
        requestAnimationFrame(animate);
    }

    // Cursor Follower (LERP)
    const cursor = document.getElementById('cursor');
    const follower = document.getElementById('cursor-follower');
    document.addEventListener('mousemove', (e) => {
        cursor.style.left = e.clientX + 'px';
        cursor.style.top = e.clientY + 'px';
        setTimeout(() => {
            follower.style.left = (e.clientX - 11) + 'px';
            follower.style.top = (e.clientY - 11) + 'px';
        }, 50);
    });

    // UI Logic
    function openNode(title) {
        document.getElementById('omniTitle').innerText = title;
        document.getElementById('omniContent').innerHTML = '<div style="display:grid; grid-template-columns: repeat(auto-fill, minmax(100px, 1fr)); gap:10px; margin-top:20px;">' + 
            Array(100).fill().map((_, i) => `<div style="background:rgba(255,255,255,0.05); padding:20px; border-radius:10px; font-size:0.6rem; border:1px solid rgba(255,255,255,0.1)">NODE_DATA_0${i+1}</div>`).join('') + 
            '</div>';
        document.getElementById('omni-slider').classList.add('active');
    }

    function showPublish() {
        document.getElementById('omniTitle').innerText = 'نشر مخطوطة جديدة';
        document.getElementById('omniContent').innerHTML = `
            <form class="publish-form" action="/submit" method="POST">
                <input type="text" name="name" placeholder="الاسم الرباعي للباحث" required>
                <input type="text" name="degree" placeholder="المؤهل العلمي" required>
                <input type="text" name="title" placeholder="عنوان العمل الأكاديمي" required>
                <select name="type">
                    <option>بحث محكم</option>
                    <option>كتاب</option>
                    <option>مقال دولي</option>
                </select>
                <input type="email" name="email" placeholder="البريد الإلكتروني الرسمي" required>
                <button type="submit" class="btn-submit">تشفير وإرسال إلى المصفوفة</button>
            </form>
        `;
        document.getElementById('omni-slider').classList.add('active');
    }

    function closeNode() { document.getElementById('omni-slider').classList.remove('active'); }

    window.addEventListener('resize', initCanvas);
    initCanvas();
    animate();
</script>

</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)

@app.route('/submit', methods=['POST'])
def submit():
    data = request.form
    print(f"[*] New Submission: {data['name']} - {data['title']}")
    return "<h1>تم استلام البيانات بنجاح وتشفيرها في الأرشيف!</h1><a href='/'>العودة للمصفوفة</a>"

if __name__ == '__main__':
    app.run(debug=True)

