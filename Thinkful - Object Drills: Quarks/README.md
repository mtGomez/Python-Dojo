<div class="markdown prose max-w-none" id="description"\><h2 id="background"\>Background</h2\>

<p\>You're modelling the interaction between a large number of quarks and have decided to create a <code\>Quark</code\> class so you can generate your own quark objects.</p\>

<p\><a href="https://en.wikipedia.org/wiki/Quark" target="\_blank"\>Quarks</a\> are fundamental particles and the only fundamental particle to experience all four fundamental forces.</p\>

<h2 id="your-task"\>Your task</h2\>

<p\>Your <code\>Quark</code\> class should allow you to create quarks of any valid color (<code\>"red"</code\>, <code\>"blue"</code\>, and <code\>"green"</code\>) and any valid flavor (<code\>'up'</code\>, <code\>'down'</code\>, <code\>'strange'</code\>, <code\>'charm'</code\>, <code\>'top'</code\>, and <code\>'bottom'</code\>).</p\>

<p\>Every quark has the same <code\>baryon\_number</code\> (<code\>BaryonNumber</code\> in <code\>C\#</code\>): 1/3.</p\>

<p\>Every quark should have an <code\>.interact()</code\> (<code\>.Interact()</code\> in <code\>C\#</code\>) method that allows any quark to interact with another quark via the strong force. When two quarks interact they exchange colors.</p\>

<h2 id="example"\>Example</h2\>

<pre\><code class="language-python"\><span class="cm-operator"\>&gt;&gt;&gt;</span\> <span class="cm-variable"\>q1</span\> <span class="cm-operator"\>=</span\> <span class="cm-variable"\>Quark</span\>(<span class="cm-string"\>"red"</span\>, <span class="cm-string"\>"up"</span\>)

<span class="cm-operator"\>&gt;&gt;&gt;</span\> <span class="cm-variable"\>q1</span\>.<span class="cm-property"\>color</span\>

<span class="cm-string"\>"red"</span\>

<span class="cm-operator"\>&gt;&gt;&gt;</span\> <span class="cm-variable"\>q1</span\>.<span class="cm-property"\>flavor</span\>

<span class="cm-string"\>"up"</span\>

<span class="cm-operator"\>&gt;&gt;&gt;</span\> <span class="cm-variable"\>q2</span\> <span class="cm-operator"\>=</span\> <span class="cm-variable"\>Quark</span\>(<span class="cm-string"\>"blue"</span\>, <span class="cm-string"\>"strange"</span\>)

<span class="cm-operator"\>&gt;&gt;&gt;</span\> <span class="cm-variable"\>q2</span\>.<span class="cm-property"\>color</span\>

<span class="cm-string"\>"blue"</span\>

<span class="cm-operator"\>&gt;&gt;&gt;</span\> <span class="cm-variable"\>q2</span\>.<span class="cm-property"\>baryon\_number</span\>

<span class="cm-number"\>0.3333333333333333</span\>

<span class="cm-operator"\>&gt;&gt;&gt;</span\> <span class="cm-variable"\>q1</span\>.<span class="cm-property"\>interact</span\>(<span class="cm-variable"\>q2</span\>)

<span class="cm-operator"\>&gt;&gt;&gt;</span\> <span class="cm-variable"\>q1</span\>.<span class="cm-property"\>color</span\>

<span class="cm-string"\>"blue"</span\>

<span class="cm-operator"\>&gt;&gt;&gt;</span\> <span class="cm-variable"\>q2</span\>.<span class="cm-property"\>color</span\>

<span class="cm-string"\>"red"</span\></code\></pre\>

<pre style="display: none;"\><code class="language-csharp"\><span class="cm-operator"\>&gt;&gt;&gt;</span\> <span class="cm-variable"\>Quark</span\> <span class="cm-variable"\>q1</span\> <span class="cm-operator"\>=</span\> <span class="cm-keyword"\>new</span\> <span class="cm-variable"\>Quark</span\>(<span class="cm-string"\>"red"</span\>, <span class="cm-string"\>"up"</span\>);

<span class="cm-operator"\>&gt;&gt;&gt;</span\> <span class="cm-variable"\>q1</span\>.<span class="cm-variable"\>Color</span\>;

<span class="cm-string"\>"red"</span\>

<span class="cm-operator"\>&gt;&gt;&gt;</span\> <span class="cm-variable"\>Quark</span\> <span class="cm-variable"\>q2</span\> <span class="cm-operator"\>=</span\> <span class="cm-keyword"\>new</span\> <span class="cm-variable"\>Quark</span\>(<span class="cm-string"\>"blue"</span\>, <span class="cm-string"\>"strange"</span\>);

<span class="cm-operator"\>&gt;&gt;&gt;</span\> <span class="cm-variable"\>q2</span\>.<span class="cm-variable"\>Color</span\>;

<span class="cm-string"\>"blue"</span\>

<span class="cm-operator"\>&gt;&gt;&gt;</span\> <span class="cm-variable"\>q2</span\>.<span class="cm-variable"\>BaryonNumber</span\>;

<span class="cm-number"\>0.3333333333333333</span\>

<span class="cm-operator"\>&gt;&gt;&gt;</span\> <span class="cm-variable"\>q1</span\>.<span class="cm-variable"\>Interact</span\>(<span class="cm-variable"\>q2</span\>);

<span class="cm-operator"\>&gt;&gt;&gt;</span\> <span class="cm-variable"\>q1</span\>.<span class="cm-variable"\>Color</span\>;

<span class="cm-string"\>"blue"</span\>

<span class="cm-operator"\>&gt;&gt;&gt;</span\> <span class="cm-variable"\>q2</span\>.<span class="cm-variable"\>Color</span\>;

<span class="cm-string"\>"red"</span\></code\></pre\>

</div\>
